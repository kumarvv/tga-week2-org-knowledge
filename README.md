# Organization Knowledge: Vector RAG vs Graph RAG

Compare answers to organizational knowledge questions using the same mock data about people, skills, projects, documents, and decisions:

- **Vector RAG:** retrieve similar text records from Chroma (local) or Pinecone (cloud), then generate an answer.
- **Graph RAG:** find semantic matches in Neo4j vector indexes, expand relationships up to two hops, then generate an answer from the connected evidence.

`compare.py` currently compares **Chroma against Neo4j**. It measures latency and uses an LLM judge to assess answer quality against the original mock data.

## 1. Set up the environment

Prerequisites:

- Python **3.12** and `uv`.
- An OpenAI API key with access to the embedding and reasoning models configured in `configs.py`.
- A running Neo4j instance supporting vector indexes, with a database named `neo4j`.
- Optional: a Pinecone account and an existing dense vector index for the cloud vector workflow.

Run all commands from the repository root so the scripts find the same local Chroma directory and `.env` file.

```sh
uv sync
```

Create a `.env` file in the repository root, or add these entries to an existing one:

```dotenv
OPENAI_API_KEY=your-openai-api-key

NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-neo4j-password

# Optional: only needed for Pinecone
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_INDEX=org-knowledge
PINECONE_NAMESPACE=mock-data
```

For a hosted Neo4j instance, use its supplied URI and credentials. The loaders and query scripts load `.env` automatically; `.env` is excluded from Git.

The defaults in `configs.py` are:

| Setting                              | Default                  |
| ------------------------------------ | ------------------------ |
| Embedding model                      | `text-embedding-3-small` |
| Embedding dimensions                 | `1024`                   |
| Reasoning model and comparison judge | `gpt-5-mini`             |
| Chroma persistence directory         | `./chromadb`             |

Use the same embedding model and dimensions for loading and querying. If you change them, rebuild the affected vector stores and Neo4j vector indexes with matching dimensions. API calls and hosted storage may incur charges.

## 2. Load the vector data

Both dedicated vector loaders read `mock_data/`, use existing document chunks, and embed the records with OpenAI.

### Option A: Chroma (required for the current comparison script)

```sh
uv run python load_vectors_chroma.py
```

This creates or updates the local collection `org_knwoledge` in `./chromadb`. The collection name is intentionally shown exactly as spelled in the code; the loader and query script use the same name. No separate Chroma server is required.

Test retrieval and answer generation with the built-in example question:

```sh
uv run python rag_vector_chroma.py
```

### Option B: Pinecone

Create a Pinecone dense vector index with **1024 dimensions** and a cosine metric to match the default OpenAI embeddings. Set `PINECONE_INDEX` to its name and set the same `PINECONE_NAMESPACE` for loading and querying. The loader expects the index to exist; it does not create one or use Pinecone-hosted embedding inference.

Validate the mock records without API calls:

```sh
uv run python load_vectors_pinecone.py --dry-run
```

**Enable uploads before loading.** In `load_vectors_pinecone.py`, inside `load_vectors_pinecone()`, replace the `record_ids = []` placeholder and commented upload block with:

```python
record_ids = vector_store.add_documents(
    documents=documents,
    ids=[document.id for document in documents],
    batch_size=32,
)
```

Then load and test:

```sh
uv run python load_vectors_pinecone.py
uv run python rag_vector_pinecone.py
```

Without that edit, the loader reports zero indexed records. Its `--batch-size` argument is currently validated but is not passed to the upload function; the snippet above sets the upload batch size explicitly.

Pinecone can be queried independently, but changing `Config.vector_platform` does **not** switch `compare.py` to Pinecone. That script calls `query_vector_chroma` directly. Comparing Pinecone against graph retrieval requires changing that import/call and adding callback support to `query_vector_pinecone` to match the comparison interface.

Use these dedicated loaders rather than the older `load_vectors.py`, whose upload calls are commented out.

## 3. Load the graph into Neo4j

Start Neo4j and check that the `.env` credentials point to the intended instance, then run:

```sh
uv run python load_graph.py
```

The loader creates uniqueness constraints and a cosine vector index for each entity label (`People`, `Skills`, `Projects`, `Documents`, and `Decisions`). It embeds the entities, upserts their properties, and loads document chunks and directed relationships.

In Neo4j Browser or your Neo4j query interface, check that all vector indexes are `ONLINE` before querying:

```cypher
SHOW VECTOR INDEXES;
```

Inspect a sample of the loaded relationships:

```cypher
MATCH (a)-[r]->(b)
RETURN a, r, b
LIMIT 50;
```

Test graph retrieval and answer generation:

```sh
uv run python rag_graph.py
```

Loaders use stable IDs to update matching records on reruns. They do not automatically remove records or relationships deleted from the mock source data.

## 4. Run the comparison

After loading **Chroma and Neo4j**, try one question first:

```sh
uv run python compare.py --limit 1
```

Run all currently enabled questions (10):

```sh
uv run python compare.py
```

Edit `QUESTIONS` in `compare.py` to change the benchmark. For each question, the script runs both approaches, alternates their execution order, and asks an LLM judge to compare the answers against the mock source data.

## 5. Inspect the results

Open **[Comparison.md](Comparison.md)** in your editor's Markdown preview after the run. Each run overwrites this report in the current working directory.

**Filename note:** the repository also contains `Comparision.md` (different spelling). The current script writes `Comparison.md`, with a capital `C`, rather than updating `Comparision.md` or lowercase `comparison.md`.

The generated report includes a win/tie summary, the executed questions, and a table containing:

| Column                 | Meaning                                                                   |
| ---------------------- | ------------------------------------------------------------------------- |
| Question               | The question sent to both approaches                                      |
| RAG Vector / RAG Graph | Full generated answers or individual errors                               |
| Time to first token    | Elapsed retrieval and generation time until the first streamed text token |
| Total Time             | End-to-end retrieval and answer generation time                           |
| Which Approach Wins    | Judge verdict and a brief explanation based on source-grounded quality    |

Judge time is excluded from the reported timings. `N/A` means no streamed text token was received. `Not evaluated` means an approach failed or the judge could not return a verdict. Winners reflect LLM quality assessments rather than speed rankings; results can vary between runs.

## Troubleshooting

- **Empty Chroma results:** run `load_vectors_chroma.py` and confirm you are querying from the same repository root using the same persistence directory.
- **Pinecone reports zero indexed records:** enable the upload block described above. Check that the index dimensions, name, and namespace match the loader and query configuration.
- **Neo4j connection or authentication error:** check the server, URI, username, password, and availability of the `neo4j` database.
- **Missing or unavailable Neo4j vector indexes:** run `load_graph.py`, then check `SHOW VECTOR INDEXES` and wait for `ONLINE` status.
- **OpenAI authentication or model errors:** check `OPENAI_API_KEY` and account access to the models in `configs.py`.
- **Unexpected or missing report:** wait for the run to finish and open `Comparison.md` in the directory where you ran the command. Individual retrieval or judge failures are recorded in the report.
