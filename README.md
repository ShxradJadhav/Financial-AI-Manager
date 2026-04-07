# Financial Document Management with AI Search

A FastAPI-based system for managing financial documents using **MySQL** for metadata and **Qdrant** for Semantic AI Search.

## Features
- **Semantic Search:** Find documents by meaning (e.g., search "debt" to find "leverage").
- **FastAPI Backend:** High-performance API with automatic Swagger documentation.
- **RAG Integration:** Uses LangChain and Sentence-Transformers for document indexing.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `.\venv\Scripts\activate`
4. Install libraries: `pip install -r requirements.txt`
5. Update `database.py` with your MySQL credentials.
6. Run the app: `uvicorn main:app --reload`
7. Open: `http://127.0.0.1:8000/docs`