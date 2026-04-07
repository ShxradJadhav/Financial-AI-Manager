from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import rag_engine  # <--- Make sure the # is gone!
from database import engine, get_db

# 1. This creates your MySQL tables
models.Base.metadata.create_all(bind=engine)

# 2. Start the App
app = FastAPI(title="Financial Doc AI")

@app.get("/")
def home():
    return {"message": "System is Online", "database": "MySQL Connected"}

@app.post("/documents/upload")
async def upload_doc(title: str, company: str, content: str, db: Session = Depends(get_db)):
    # Save to MySQL (The Metadata)
    new_doc = models.FinancialDocument(
        title=title, 
        company_name=company,
        document_type="report",
        uploaded_by="Admin"
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    
    # Save to Qdrant (The AI Meaning) <--- ADD THIS LINE
    rag_engine.index_document(content, new_doc.id, title)
    
    return {"status": "Saved to MySQL and AI Search!", "id": new_doc.id}

@app.get("/rag/search")
def ai_search(query: str):
    # This calls the "Search" function from your rag_engine.py file
    results = rag_engine.search_docs(query)
    
    # We return the parts of the document the AI found most relevant
    return [{"content": res.page_content, "metadata": res.metadata} for res in results]