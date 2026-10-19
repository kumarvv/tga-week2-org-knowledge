import os 
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain.messages import AIMessage
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import Pinecone as PineconeVectorStore
from pinecone import Pinecone 

load_dotenv()

def query_vector_pinecone(embeddings_model: OpenAIEmbeddings, query: str) -> list[Document]: 
    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index(os.getenv("PINECONE_INDEX"))

    vector_store = PineconeVectorStore(
        index=index, 
        embedding=embeddings_model,
        namespace=os.getenv("PINECONE_NAMESPACE")
    )

    vector_retriever = vector_store.as_retriever(kwargs={"k":5})
    retrieved_docs = vector_retriever.invoke(query)

    return retrieved_docs


def ask_question_vector(question: str) -> AIMessage: 
    # retrieved_docs = vector_store.similarity_search(question, k=5)

    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
    prompt = RAG_TEMPLATE.invoke({"question": question, "context": docs_content})
    #print(f"PROMPT: {prompt.to_string()}")

    response = llm.invoke(prompt)

    return response

def query_vector(query: str) -> AIMessage: 
    # searches using pinecone cloud vector store 
    embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)  # 512-dim vectors


    llm = ChatOpenAI(model="gpt-5-mini")
    template = """You are an organizational knowledge assistant. Answer questions about people, skills, projects, documents, and decisions using the organization’s data indexed in Pinecone.

    CONTEXT: {context}

    QUESTION: {question}
    """
    RAG_TEMPLATE = PromptTemplate.from_template(template)

    # use pinecone vector store 
    query_vector_pinecone()



def main(): 
    q = "What documents has Elena Rossi written about search quality, and what evidence or evaluation methods do they contain?"
    response = ask_question_vector(q)

    print(response.content)


if __name__ == "__main__": 
    main()