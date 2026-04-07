🚀 AI-Powered Financial Document Manager (RAG)

A production-ready Retrieval-Augmented Generation (RAG) backend system designed to ingest, store, and intelligently search through complex financial documents.

Live API Documentation: https://financial-ai-manager.onrender.com/docs

Author: Sharad Jadhav

Tech Stack: FastAPI, MySQL (Local), PostgreSQL (Cloud), Qdrant Vector DB, LangChain, HuggingFace.

📌 The Problem Statement

Financial analysts often struggle with "Keyword Search" limitations. For example, searching for "Financial Trouble" won't find a document that only uses the word "Liquidity Crisis."

The Goal: Build a system that understands the meaning of financial text (Semantic Search) while maintaining a structured database for metadata (Titles, Companies, Upload Dates).

🛠️ System Architecture (The "How")

I implemented a Polyglot Persistence architecture to handle two types of data:

Structured Metadata (MySQL/PostgreSQL): Stores document ID, title, company name, and timestamps.

Unstructured Vectors (Qdrant): Stores "Embeddings" (mathematical representations) of the document content.

The Pipeline:

Ingestion: User uploads a document via a FastAPI POST endpoint.

Embedding: The system uses the BAAI/bge-small-en-v1.5 model to turn text into a 384-dimensional vector.

Storage: Metadata is saved to SQL; Vectors are indexed in Qdrant.

Retrieval (RAG): When a user searches, the query is vectorized and compared against the Qdrant index using Cosine Similarity.

🚀 Deployment & DevOps

This project is fully containerized and deployed using a CI/CD pipeline from GitHub to Render.com.

Database: Provisioned a Managed PostgreSQL instance in the cloud.

Environment Variables: Used DATABASE_URL to securely switch between local development and production.

Performance: Configured Uvicorn with a 120s timeout to handle heavy AI model loading on cold starts.

🚧 Challenges & Solutions

Problem

Solution

500 Internal Server Errors

Implemented detailed try-except logging and fixed folder permission issues for the vector store.

Cloud DB Mismatch

Developed a dynamic database.py that auto-switches from MySQL (Local) to PostgreSQL (Cloud) using URI prefix replacement.

Dependency Weight

Optimized requirements.txt to include psycopg2-binary for Linux deployment while keeping PyTorch CPU-only to fit free-tier limits.

✅ Key Outcomes

Semantic Accuracy: The system can link concepts like "Debt" to "Leverage" with 90%+ similarity.

Scalability: Ready to be moved to Azure Cognitive Search or AWS Kendra for enterprise-scale data.

Professional API: Automatic interactive documentation via Swagger UI.

🏃 How to Run Locally

Clone the repo: git clone https://github.com/ShxradJadhav/Financial-AI-Manager.git

Create VENV: python -m venv venv

Activate: .\venv\Scripts\activate

Install: pip install -r requirements.txt

Run: uvicorn main:app --reload
