from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")


client = QdrantClient(path="./qdrant_db") 
collection_name = "financial_docs"

def index_document(text: str, doc_id: int, title: str):
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    

    docs = [Document(page_content=chunk, metadata={"doc_id": doc_id, "title": title}) for chunk in chunks]
    
    
    QdrantVectorStore.from_documents(
        docs,
        embeddings,
        path="./qdrant_db",
        collection_name=collection_name,
    )
    return "Indexed successfully!"

def search_docs(query: str):
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
        embeddings=embeddings,
    )
    results = vector_store.similarity_search(query, k=3)
    return results
