# 🎓 AI Study Abroad Assistant — Backend (FastAPI)

This repository contains the **backend service** for the AI-powered Study Abroad Assistant application.  
It provides APIs for authentication, AI-based chat interaction, and document uploads, helping students explore study-abroad opportunities intelligently.

---

## 🚀 Live API & Documentation

- **Base URL:**  
  👉 [https://ai-study-abroad-backend.onrender.com](https://ai-study-abroad-backend.onrender.com)

- **Interactive API Docs (Swagger UI):**  
  👉 [https://ai-study-abroad-backend.onrender.com/docs](https://ai-study-abroad-backend.onrender.com/docs)

---

## 🧩 Key Features

✅ **User Authentication** – Register and login securely with JWT tokens  
✅ **AI Chat Assistant** – Get real-time guidance using AI models  
✅ **Document Upload** – Upload and analyze PDFs for study recommendations  
✅ **Chat History** – Retrieve past user–AI conversations  
✅ **CORS Enabled** – Fully integrated with the Next.js frontend  
✅ **Deployed on Render** – Always-on public API endpoint  

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| Framework | **FastAPI** |
| Language | **Python 3.13** |
| Database | SQLite (for dev) / PostgreSQL (for production) |
| Authentication | JWT (JSON Web Token) |
| Hashing | Passlib + bcrypt |
| AI API | Groq / OpenAI API |
| Deployment | Render (free tier) |

---

## ⚙️ Setup Instructions (Run Locally)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Bhavana546/ai_study_abroad_backend.git
cd ai_study_abroad_backend
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # For Windows
# OR
source venv/bin/activate  # For macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI server

```bash
uvicorn app.main:app --reload
```

Now visit 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔑 Environment Variables

Create a `.env` file inside the project root:

```bash
SECRET_KEY=your_secret_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
AI_API_KEY=your_groq_or_openai_key
```

---

## 📄 API Endpoints Overview

| Endpoint        | Method | Description                |
| --------------- | ------ | -------------------------- |
| `/auth/signup`  | POST   | Register a new user        |
| `/auth/login`   | POST   | Login user and return JWT  |
| `/docs/upload`  | POST   | Upload a PDF document      |
| `/chat/ask`     | POST   | Ask AI-based question      |
| `/chat/history` | GET    | Retrieve past chat history |
| `/`             | GET    | Health check endpoint      |

---

## 🧠 Example Request

### Signup Example:

```bash
POST /auth/signup
{
  "name": "Bhavana Kolluri",
  "email": "bhavana.demo@gmail.com",
  "password": "Bhavana@123"
}
```

✅ **Response**

```json
{
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

---

## 🖼️ Screenshots (Add After Deployment)
<img width="1919" height="1012" alt="Screenshot 2025-11-12 124441" src="https://github.com/user-attachments/assets/72367415-d4aa-4ed0-910c-cd0562e65f14" />


<img width="1919" height="971" alt="Screenshot 2025-11-12 172545" src="https://github.com/user-attachments/assets/17583ae6-c436-4582-8b4b-f895dbd85e55" />


<img width="1538" height="640" alt="Screenshot 2025-11-12 134233" src="https://github.com/user-attachments/assets/609b1fc5-487e-46a3-a399-fe0e33ceef8f" />




---

## 🧩 Project Structure

```
ai_study_abroad_backend/
│
├── app/
│   ├── api/              # API routes
│   ├── core/             # Security, JWT, and hashing logic
│   ├── models/           # Database models (User, Chat, etc.)
│   ├── main.py           # FastAPI app entry point
│   └── schemas.py        # Pydantic schemas
│
├── .env.example          # Example environment variables
├── requirements.txt      # Dependencies list
└── README.md             # Project documentation
```

---

## ☁️ Deployment

This backend is deployed on **Render**.

🔹 **Live API:**
[https://ai-study-abroad-backend.onrender.com](https://ai-study-abroad-backend.onrender.com)

🔹 **Interactive Docs:**
[https://ai-study-abroad-backend.onrender.com/docs](https://ai-study-abroad-backend.onrender.com/docs)

---

## 🎥 Demo Video

🎬 *Watch the full demo here:*


https://github.com/user-attachments/assets/37717f03-5edd-421f-bc7c-dd481efbec32



---

## 👩‍💻 Author

**Bhavana Kolluri**
🎓 B.Tech CSE (AI & Data Science) — Siddhartha Academy of Higher Education
📧 **Email:** [bhavana.demo@gmail.com](mailto:bhavana.demo@gmail.com)
💼 [LinkedIn](https://www.linkedin.com/in/bhavana-kolluri)
🌐 [GitHub](https://github.com/Bhavana546)

---

⭐ *Built with ❤️ using FastAPI, Passlib, and JWT Authentication — deployed on Render.*

```

2. Make the frontend README slightly simpler and UI-focused?
```
