# 🚀 Financial-AI-Manager (RAG Backend)

A production-ready **Retrieval-Augmented Generation (RAG)** system built to ingest, store, and intelligently search financial documents using Semantic AI.

**Live Link:** [https://financial-ai-manager.onrender.com/docs](https://financial-ai-manager.onrender.com/docs)  
**Interactive Documentation:** http://127.0.0.1:8000/docs#/

**Developer:** Sharad Jadhav  
**Tech:** FastAPI | MySQL (Local) | PostgreSQL (Cloud) | Qdrant Vector DB | LangChain

---
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8949a384-3df4-49c0-8a3d-3ca787c7a5d8" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d82227b4-ad4d-49a2-9dcc-4302c6185deb" />

## 📌 Project Overview
This project solves the "Keyword Gap" in financial analysis. Instead of just searching for exact words, this system uses **Vector Embeddings** to understand financial context.

### Key Features:
- **Semantic Search:** Searching for "borrowing issues" will find documents containing "liquidity crisis" or "high leverage."
- **Polyglot Persistence:** Uses **SQL** for structured metadata and **Vector DB** for unstructured text meaning.
- **Auto-Documentation:** Built-in Swagger UI for easy API testing.

---

## 🏗️ System Architecture
The data flows through a modern AI pipeline:

1. **Ingestion Layer:** FastAPI receives the document title, company, and content.
2. **Database Sink (SQL):** Metadata is stored in **PostgreSQL** (Render) or **MySQL** (Local).
3. **Embedding Engine:** `BAAI/bge-small-en-v1.5` turns text into 384-dimensional vectors.
4. **Vector Store:** Vectors are indexed in **Qdrant** for high-speed similarity searching.



---

## 🛠️ Tech Stack & Skills
- **Framework:** FastAPI (Python)
- **Database:** MySQL, SQLAlchemy ORM, PostgreSQL
- **AI/ML:** LangChain, HuggingFace Embeddings, Sentence-Transformers
- **Vector Store:** Qdrant (Local & Cloud-ready)
- **DevOps:** Git, GitHub, Render (Cloud Deployment)

---

## 🚧 Challenges Faced & Problem Solving

### 1. Database Portability (MySQL to Postgres)
* **Problem:** Developed locally on MySQL, but cloud providers use PostgreSQL.
* **Solution:** Rewrote `database.py` to use dynamic environment variables (`DATABASE_URL`) and added logic to automatically fix URI prefixes for SQLAlchemy compatibility.

### 2. Cold-Start Model Loading
* **Problem:** The 500MB AI model caused the server to time out on the first request.
* **Solution:** Increased Uvicorn timeout settings and implemented a "Lazy Loading" strategy for the HuggingFace model.

### 3. Dependency Conflicts
* **Problem:** Python 3.14.x on the cloud had conflicts with older AI libraries.
* **Solution:** Optimized `requirements.txt` to use `psycopg2-binary` and forced specific versions of `torch` to fit within Render's free-tier RAM limits.

---

## 🚀 How to Run Locally

1. **Clone & Setup:**
   ```bash
   git clone [https://github.com/ShxradJadhav/Financial-AI-Manager.git](https://github.com/ShxradJadhav/Financial-AI-Manager.git)
   cd Financial-AI-Manager
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
