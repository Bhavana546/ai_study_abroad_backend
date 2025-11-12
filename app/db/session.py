from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database path
SQLALCHEMY_DATABASE_URL = "sqlite:///./studyabroad.db"

# For SQLite, this must be set like this:
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal is the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()

# ✅ Dependency for FastAPI routes
def get_db():
    """Create and close DB session automatically in routes."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
