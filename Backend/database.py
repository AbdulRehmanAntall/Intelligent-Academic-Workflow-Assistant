from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker    
import os

# Database URL from environment variable or default to SQLite
SQLALCHEMY_DATABASE_URL='postgresql://postgres:789645@localhost/ToDoAPP'

# Create the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base class for declarative models
Base = declarative_base()


def get_db():
    """
    Dependency to get a database session.
    Yields a database session and ensures it is closed after use.
    """
    db = session_local()
    try:
        yield db
    finally:
        db.close()