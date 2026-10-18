"""Embed the organization mock data and store it in Pinecone."""

import argparse
import os
from collections import Counter
from typing import Any
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import Pinecone as PineconeVectorStore
from langchain_chroma import Chroma
from pinecone import Pinecone 
import chromadb 

from mock_data.decisions import DECISIONS
from mock_data.documents import DOCUMENTS
from mock_data.people import PEOPLE
from mock_data.projects import PROJECTS
from mock_data.skills import SKILLS

MODEL = "llama-text-embed-v2"
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

def load_pinecone(embeddings: OpenAIEmbeddings, documents: list[Document]) -> list[str]: 
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", default=os.getenv("PINECONE_INDEX", "org-knowledge"))
    parser.add_argument("--namespace", default=os.getenv("PINECONE_NAMESPACE", "mock-data"))
    parser.add_argument("--cloud", default=os.getenv("PINECONE_CLOUD", "aws"))
    parser.add_argument("--region", default=os.getenv("PINECONE_REGION", "us-east-1"))
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--dry-run", action="store_true", help="Validate records without API calls")
    args = parser.parse_args()
    if not 1 <= args.batch_size <= 96:
        parser.error("--batch-size must be between 1 and 96")
    if not args.namespace.strip():
        parser.error("--namespace must not be empty")

    # Pinecone 
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index(api_key=os.getenv("PINECONE_INDEX"))

    vector_store = PineconeVectorStore(
        index=index, 
        embedding=embeddings,
        namespace=args.namespace
    )

    print(f"Indexing {len(documents)} records")
    
    ### PINECONE -- ONETIME RUN ONLY -- UNCOMMENT WHEN NEEDED 
    record_ids = vector_store.add_documents(
        documents=documents,
        ids=[document.id for document in documents],
        batch_size=args.batch_size,
    )

    print(f"Completed indexing {len(record_ids)} records")
    return record_ids


def load_chromadb(embeddings: OpenAIEmbeddings, documents: list[Document]) -> None: 
    PERSIST_DIR = "./chromadb"

    vector_store = Chroma(
        collection_name="org_knwoledge",
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR,
    )

    vector_store.add_documents(
        ids=[document.id for document in documents],
        documents=documents
    )


def main() -> None:
    """Embed mock records with OpenAI and upload to an existing Pinecone index."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--dry-run", action="store_true", help="Validate records without API calls")
    args = parser.parse_args()
    if not 1 <= args.batch_size <= 96:
        parser.error("--batch-size must be between 1 and 96")

    records = build_records()
    counts = Counter(record["entity_type"] for record in records)
    print(f"Prepared {len(records)} records: {dict(counts)}")
    if args.dry_run:
        return

    documents = build_documents(records=records)

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)

    # NOTE: run once during inital load. choose local (Chroma) or cloud (Pinecone)

    # Pinecone cloud
    # load_pinecone(embeddings=embeddings, documents=documents)

    # chroma db 
    # load_chromadb(embeddings=embeddings, documents=documents)

    

if __name__ == "__main__":
    main()
