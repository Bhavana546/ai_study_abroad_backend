from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from groq import Groq
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.chat_history import ChatHistory
import os

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    question: str
    country: str
    user: str | None = None  # optional user name or email

@router.get("/")
async def test_chat():
    return {"message": "Chat API working!"}

@router.post("/ask")
async def ask_question(q: ChatRequest, db: Session = Depends(get_db)):
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="Missing GROQ_API_KEY")

    client = Groq(api_key=GROQ_API_KEY)

    models_to_try = [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "meta-llama/llama-4-maverick-17b-128e-instruct"
    ]

    system_prompt = (
        f"You are Bhavana's AI Study Abroad Assistant. "
        f"Answer based only on study abroad documents for {q.country}."
    )

    for model in models_to_try:
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": q.question}
                ],
                temperature=0.3,
                max_tokens=400
            )

            answer = completion.choices[0].message.content

            # ✅ Save the chat in database
            chat_entry = ChatHistory(
                user=q.user,
                country=q.country,
                question=q.question,
                answer=answer,
                model_used=model
            )
            db.add(chat_entry)
            db.commit()
            db.refresh(chat_entry)

            return {
                "message": "Chat saved successfully",
                "model_used": model,
                "country": q.country,
                "question": q.question,
                "answer": answer
            }

        except Exception as e:
            print(f"⚠️ Model {model} failed: {e}")
            continue

    raise HTTPException(status_code=500, detail="All models failed.")

@router.get("/history")
async def get_history(db: Session = Depends(get_db)):
    """Get all chat history entries"""
    history = db.query(ChatHistory).order_by(ChatHistory.timestamp.desc()).all()
    return [
        {
            "id": h.id,
            "user": h.user,
            "country": h.country,
            "question": h.question,
            "answer": h.answer,
            "model_used": h.model_used,
            "timestamp": h.timestamp
        }
        for h in history
    ]
