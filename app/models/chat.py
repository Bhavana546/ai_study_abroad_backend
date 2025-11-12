from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.dialects.sqlite import JSON
from app.db.session import Base

class Chat(Base):
    __tablename__ = "chat_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question = Column(Text)
    answer = Column(Text)
    sources = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
