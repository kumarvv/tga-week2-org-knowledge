
"""Load organization entities, relationships, and embeddings into Neo4j."""

import os
import re
from collections import defaultdict

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from neo4j import GraphDatabase, Driver

from configs import Config, get_config

from mock_data.decisions import DECISIONS
from mock_data.documents import DOCUMENTS
from mock_data.people import PEOPLE
from mock_data.projects import PROJECTS
from mock_data.skills import SKILLS

load_dotenv()

ENTITY_GROUPS = {
    "People": PEOPLE,
    "Skills": SKILLS,
    "Projects": PROJECTS,
    "Documents": DOCUMENTS,
    "Decisions": DECISIONS,
}

def get_neo4j_driver() -> Driver:
    """Initializes and returns the Neo4j driver."""
    uri = os.getenv("NEO4J_URI")
    user = os.getenv("NEO4J_USERNAME")
    password = os.getenv("NEO4J_PASSWORD")

    return GraphDatabase.driver(uri, auth=(user, password))

def setup_neo4j_constraints(driver: Driver):
    """Adds unique constraints to the Neo4j database to prevent duplicate nodes."""
    with driver.session(database="neo4j") as session:
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (c:People) REQUIRE c.id IS UNIQUE")
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (c:Skills) REQUIRE c.id IS UNIQUE")
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (r:Projects) REQUIRE r.id IS UNIQUE")
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (s:Documents) REQUIRE s.id IS UNIQUE")
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (s:Decisions) REQUIRE s.id IS UNIQUE")
        session.run("CREATE CONSTRAINT IF NOT EXISTS FOR (c:Chunk) REQUIRE c.id IS UNIQUE")
    print("Neo4j constraints are set.")

def create_vector_index(driver: Driver, embedding_model):
    """Create a cosine vector index for each imported entity label."""
    vector_dimensions = len(embedding_model.embed_query("sample"))
    if not vector_dimensions:
        raise ValueError("The embedding model returned an empty vector")

    with driver.session(database="neo4j") as session:
        for label in ENTITY_GROUPS:
            session.run(f"""
                CREATE VECTOR INDEX `org_knowledge_{label.lower()}` IF NOT EXISTS
                FOR (n:{label}) ON (n.embedding)
                OPTIONS {{ indexConfig: {{
                    `vector.dimensions`: {vector_dimensions},
                    `vector.similarity_function`: 'cosine'
                }} }}
            """).consume()
    print("Vector indexes for all five entity labels are set.")


def ingest_data(driver: Driver, embedding_model) -> None:
    """Upsert all mock entities, embeddings, chunks, and directed relationships.

    Flatten document access metadata onto Documents nodes and store skill
    proficiency as the level property of HAS_SKILL relationships.
    """
    labels_by_id = {}
    for label, entities in ENTITY_GROUPS.items():
        for entity in entities:
            if entity["id"] in labels_by_id:
                raise ValueError(f"Duplicate entity ID: {entity['id']}")
            labels_by_id[entity["id"]] = label

    nodes = defaultdict(list)
    relationships = defaultdict(list)
    chunks = []
    for label, entities in ENTITY_GROUPS.items():
        for entity in entities:
            levels = {
                item["skill_id"]: item["level"]
                for item in entity.get("skill_proficiencies", [])
            }
            for relationship in entity.get("relationships", []):
                kind = relationship["type"]
                if not re.fullmatch(r"[A-Z][A-Z0-9_]*", kind):
                    raise ValueError(f"Invalid relationship type: {kind}")
                target_id = relationship["target_id"]
                if target_id not in labels_by_id:
                    raise ValueError(f"Unknown relationship target: {target_id}")
                properties = {}
                if kind == "HAS_SKILL" and target_id in levels:
                    properties["level"] = levels[target_id]
                relationships[(label, kind, labels_by_id[target_id])].append({
                    "source_id": entity["id"],
                    "target_id": target_id,
                    "properties": properties,
                })
            properties = {
                key: value for key, value in entity.items()
                if key not in {"relationships", "skill_proficiencies", "access", "chunks"}
            }
            properties.update(entity.get("access", {}))
            nodes[label].append(properties)
            chunks.extend(entity.get("chunks", []))

    # Embed before opening the write transaction so API failures leave no partial load.
    for properties in nodes.values():
        vectors = embedding_model.embed_documents([
            item["retrieval_text"] for item in properties
        ])
        if len(vectors) != len(properties):
            raise ValueError("The embedding model returned the wrong number of vectors")
        for item, vector in zip(properties, vectors):
            if not vector:
                raise ValueError(f"Empty embedding for {item['id']}")
            item["embedding"] = vector

    def write_graph(tx):
        for label, rows in nodes.items():
            tx.run(f"""
                UNWIND $rows AS row
                MERGE (n:{label} {{id: row.id}})
                SET n += row
            """, rows=rows).consume()
        tx.run("""
            UNWIND $rows AS row
            MATCH (d:Documents {id: row.document_id})
            MERGE (c:Chunk {id: row.id})
            SET c += row
            MERGE (d)-[:HAS_CHUNK]->(c)
        """, rows=chunks).consume()
        for (source, kind, target), rows in relationships.items():
            tx.run(f"""
                UNWIND $rows AS row
                MATCH (source:{source} {{id: row.source_id}})
                MATCH (target:{target} {{id: row.target_id}})
                MERGE (source)-[r:{kind}]->(target)
                SET r += row.properties
            """, rows=rows).consume()

    with driver.session(database="neo4j") as session:
        session.execute_write(write_graph)
    print(f"Ingested {len(labels_by_id)} entities into Neo4j.")


def main() -> None:
    """Initialize the graph schema and ingest the organization mock data."""
    config = get_config(Config())
    embeddings = OpenAIEmbeddings(
        model=config.embeddings_model,
        dimensions=config.embeddings_dimensions,
    )
    with get_neo4j_driver() as driver:
        driver.verify_connectivity()
        setup_neo4j_constraints(driver)
        create_vector_index(driver, embeddings)
        ingest_data(driver, embeddings)


if __name__ == "__main__":
    main()
