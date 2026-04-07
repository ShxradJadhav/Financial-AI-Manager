from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(String(20), default="Client") # Admin, Analyst, Auditor, Client

class FinancialDocument(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    company_name = Column(String(100))
    document_type = Column(String(20)) # invoice, report, contract
    uploaded_by = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)