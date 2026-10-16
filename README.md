# tga-week2-org-knowledge
Organization Knowledge

## Load mock data into Pinecone

The loader uses Pinecone's hosted `llama-text-embed-v2` model to generate
embeddings during upload. It loads people, skills, projects, decisions, and
document chunks, retaining source links, access labels, and relationship IDs
as searchable metadata. No OpenAI API key is needed.

```sh
uv sync
uv run python load_vectors.py --dry-run
export PINECONE_API_KEY='your-pinecone-api-key'
uv run python load_vectors.py
```

The default index is `org-knowledge`, namespace `mock-data`, in AWS `us-east-1`.
Override these with `--index`, `--namespace`, `--cloud`, and `--region`, or the
corresponding `PINECONE_INDEX`, `PINECONE_NAMESPACE`, `PINECONE_CLOUD`, and
`PINECONE_REGION` environment variables. The script reads exported environment
variables; it does not load a `.env` file.

An index is created if needed. Existing indexes must use the same embedding
model and text field. Stable IDs make reruns overwrite matching records;
records removed from the source data are not automatically deleted.
Uploading uses Pinecone inference and storage and may incur account charges.
Access metadata is retained for retrieval filters; it does not enforce access
control on its own.

API reference: [Pinecone integrated embeddings](https://sdk.pinecone.io/python/how-to/integrated-records.html).
