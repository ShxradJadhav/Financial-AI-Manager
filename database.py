import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Get the URL from Render's environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. If no Cloud URL, use your local MySQL
if not DATABASE_URL:
    # Change 'root:root' to your local password if different
    DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/finance_db"

# 3. SQLAlchemy fix: Render gives 'postgres://', but SQLAlchemy needs 'postgresql://'
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()