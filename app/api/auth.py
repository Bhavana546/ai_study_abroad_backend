from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("/signup")
def signup(data: SignupRequest):
    print("🟢 Signup endpoint hit!")
    print("📩 Raw signup data:", data.dict())

    db = SessionLocal()

    # Check if user already exists
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        print("⚠️ Email already registered:", data.email)
        raise HTTPException(status_code=400, detail="Email already registered.")

    try:
        hashed_pw = get_password_hash(data.password)
        user = User(name=data.name, email=data.email, hashed_password=hashed_pw)
        db.add(user)
        db.commit()
        token = create_access_token({"sub": user.email})
        print("✅ User created successfully:", user.email)
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        print("❌ Signup failed with error:", str(e))
        raise HTTPException(status_code=500, detail="Server error: " + str(e))


class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    db = SessionLocal()
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
