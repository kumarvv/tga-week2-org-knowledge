from dataclasses import dataclass

CHROMA_PERSIST_DIR = "./chromadb"

@dataclass
class Config:
    embeddings_model: str = "text-embedding-3-small"
    embeddings_dimensions: int = 1024
    reasoning_model: str = "gpt-5-mini"

    rag_type: str = "vector"  # vector or graph

    vector_platform: str = "chroma"  # chroma or pinecone
    graph_platform: str = "local"  # local


def get_config(config: Config | None = None) -> Config:
    if config is None:
        return Config()

    defaults = Config()
    for name in Config.__dataclass_fields__:
        if getattr(config, name) is None:
            setattr(config, name, getattr(defaults, name))
    return config
