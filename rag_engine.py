from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# 1. This is the "Translator" that turns English into Math (Vectors)
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

# 2. Setup Qdrant (We will use a local file for now so you don't need to install a server)
client = QdrantClient(path="./qdrant_db") 
collection_name = "financial_docs"

def index_document(text: str, doc_id: int, title: str):
    # Split big text into small chunks so the AI can read it easily
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    
    # Create documents with metadata
    docs = [Document(page_content=chunk, metadata={"doc_id": doc_id, "title": title}) for chunk in chunks]
    
    # Save to Qdrant
    QdrantVectorStore.from_documents(
        docs,
        embeddings,
        path="./qdrant_db",
        collection_name=collection_name,
    )
    return "Indexed successfully!"

def search_docs(query: str):
    # This is the "Semantic Search" - it finds meaning, not just keywords
    vector_store = QdrantVectorStore(
        client=client,
        collection_name=collection_name,
        embeddings=embeddings,
    )
    results = vector_store.similarity_search(query, k=3)
    return results