import os 
from dotenv import load_dotenv

from langchain.messages import AIMessage
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma

from configs import Config, get_config, CHROMA_PERSIST_DIR

load_dotenv()

def query_vector_chroma(config: Config, question: str) -> AIMessage: 
    embeddings = OpenAIEmbeddings(model=config.embeddings_model, dimensions=config.embeddings_dimensions)  # 512-dim vectors

    vector_store = Chroma(
        collection_name="org_knwoledge",
        embedding_function=embeddings,
        persist_directory=CHROMA_PERSIST_DIR,
    )

    # retrieve docs   
    template = """You are an organizational knowledge assistant. Answer questions about people, skills, projects, documents, and decisions using the organization’s data indexed in Pinecone.

    CONTEXT: {context}

    QUESTION: {question}
    """
    RAG_TEMPLATE = PromptTemplate.from_template(template)

    vector_retriever = vector_store.as_retriever(kwargs={"k":5})
    retrieved_docs = vector_retriever.invoke(question)

    # response 
    llm = ChatOpenAI(model=config.reasoning_model)

    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
    prompt = RAG_TEMPLATE.invoke({"question": question, "context": docs_content})

    response = llm.invoke(prompt)

    return response


def main(): 
    question = "What documents has Elena Rossi written about search quality, and what evidence or evaluation methods do they contain?"
    config = get_config()

    response = query_vector_chroma(config=config, question=question)

    print(response.content)


if __name__ == "__main__": 
    main()