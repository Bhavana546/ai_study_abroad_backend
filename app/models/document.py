from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.session import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    country = Column(String, nullable=False)
    uploaded_by = Column(String, nullable=True)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
