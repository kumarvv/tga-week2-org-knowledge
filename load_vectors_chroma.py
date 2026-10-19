"""Embed the organization mock data and store it in Pinecone."""

from collections import Counter
from typing import Any
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from configs import Config, get_config, CHROMA_PERSIST_DIR

from mock_data.decisions import DECISIONS
from mock_data.documents import DOCUMENTS
from mock_data.people import PEOPLE
from mock_data.projects import PROJECTS
from mock_data.skills import SKILLS

TEXT_FIELD = "text"

load_dotenv()

def build_records() -> list[dict[str, Any]]:
    """Build flat Pinecone records, using existing chunks for documents."""
    records = []
    for entity in [*PEOPLE, *SKILLS, *PROJECTS, *DOCUMENTS, *DECISIONS]:
        metadata = {
            key: value
            for key, value in entity.items()
            if isinstance(value, (str, int, float, bool))
            and key not in {"id", "retrieval_text", "content"}
        }
        metadata["entity_id"] = entity["id"]
        for key, value in entity.get("access", {}).items():
            metadata[key] = value

        chunks = entity.get("chunks", [])
        if chunks:
            for chunk in chunks:
                records.append({
                    "id": f"document:{entity['id']}:{chunk['id']}",
                    "document_id": entity["id"],
                    "chunk_id": chunk["id"],
                    "heading": chunk["heading"],
                    TEXT_FIELD: f"{entity['name']}\n{chunk['heading']}\n{chunk['text']}",
                    "entity_type": metadata["entity_type"],
                    "metadata": metadata,
                })
        else:
            records.append({
                "id": f"{entity['entity_type']}:{entity['id']}",
                TEXT_FIELD: entity["retrieval_text"],
                "entity_type": metadata["entity_type"],
                "metadata": metadata,
            })

    ids = [record["id"] for record in records]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate vector IDs in mock data")
    if any(not record[TEXT_FIELD].strip() for record in records):
        raise ValueError("Every record must have non-empty embedding text")
    return records


def build_documents(records: list[dict[str, Any]]) -> list[Document]:
    """Convert records to LangChain documents while retaining stable IDs."""
    return [
        Document(
            id=record["id"],
            page_content=record[TEXT_FIELD],
            metadata={
                **record["metadata"],
                **{
                    key: record[key]
                    for key in ("document_id", "chunk_id", "heading")
                    if key in record
                },
            },
        )
        for record in records
    ]

def load_vectors_chroma(config: Config, documents: list[Document]) -> None: 
    embeddings = OpenAIEmbeddings(model=config.embeddings_model, dimensions=config.embeddings_dimensions)

    vector_store = Chroma(
        collection_name="org_knwoledge",
        embedding_function=embeddings,
        persist_directory=CHROMA_PERSIST_DIR,
    )

    vector_store.add_documents(
        ids=[document.id for document in documents],
        documents=documents
    )


def main() -> None:
    config = get_config(None)

    records = build_records()
    counts = Counter(record["entity_type"] for record in records)
    print(f"Prepared {len(records)} records: {dict(counts)}")

    documents = build_documents(records=records)

    # NOTE: run once during inital load. choose local (Chroma) or cloud (Pinecone)

    # local chroma 
    load_vectors_chroma(config=config, documents=documents)

    

if __name__ == "__main__":
    main()
