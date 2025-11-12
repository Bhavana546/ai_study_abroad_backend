from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import Base, engine
from app.api import auth, docs, chat

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Study Abroad Assistant")

# ✅ FIX: Add CORS middleware here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] if you want stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(docs.router)
app.include_router(chat.router)

@app.get("/")
def home():
    return {"message": "AI Study Abroad Backend is running!"}
