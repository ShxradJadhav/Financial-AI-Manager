from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# IMPORTANT: Change 'your_password' to your actual MySQL root password!
# If your MySQL port is not 3306, change that too.
# Change 'root' to 'root' if that is your password
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/finance_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This helper gets a connection to the DB and closes it when done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()