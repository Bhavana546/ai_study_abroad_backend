from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.db.session import Base

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, nullable=True)  # optional user email or name
    country = Column(String, nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    model_used = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
