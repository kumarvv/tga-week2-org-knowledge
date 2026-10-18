import os 
from dotenv import load_dotenv

from langchain.messages import AIMessage
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import Pinecone as PineconeVectorStore
from pinecone import Pinecone 

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)  # 512-dim vectors

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index(os.getenv("PINECONE_INDEX"))

vector_store = PineconeVectorStore(
    index=index, 
    embedding=embeddings,
    namespace=os.getenv("PINECONE_NAMESPACE")
)

llm = ChatOpenAI(model="gpt-5-mini")

template = """You are an organizational knowledge assistant. Answer questions about people, skills, projects, documents, and decisions using the organization’s data indexed in Pinecone.

CONTEXT: {context}

QUESTION: {question}
"""
RAG_TEMPLATE = PromptTemplate.from_template(template)

def ask_question_vector(question: str) -> AIMessage: 
    # retrieved_docs = vector_store.similarity_search(question, k=5)
    vector_retriever = vector_store.as_retriever(kwargs={"k":5})
    retrieved_docs = vector_retriever.invoke(question)

    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
    prompt = RAG_TEMPLATE.invoke({"question": question, "context": docs_content})
    #print(f"PROMPT: {prompt.to_string()}")

    response = llm.invoke(prompt)

    return response


def main(): 
    q = "What documents has Elena Rossi written about search quality, and what evidence or evaluation methods do they contain?"
    response = ask_question_vector(q)

    print(response.content)


if __name__ == "__main__": 
    main()