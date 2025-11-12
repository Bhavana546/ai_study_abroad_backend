from fastapi import APIRouter, UploadFile, File, HTTPException
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss, os
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/docs", tags=["Documents"])

INDEX_PATH = os.getenv("VECTOR_INDEX_PATH", "app/indexes/faiss.index")
METADATA_PATH = os.getenv("METADATA_PATH", "app/indexes/meta.npy")

def load_index(dim=384):
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
    else:
        index = faiss.IndexFlatL2(dim)
    return index

def split_text(text, chunk_size=600, overlap=100):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...), country: str = "USA"):
    try:
        contents = await file.read()
        reader = PdfReader(BytesIO(contents))
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"

        chunks = split_text(text)
        model = SentenceTransformer("all-MiniLM-L6-v2")
        embeddings = model.encode(chunks, convert_to_numpy=True)

        index = load_index(embeddings.shape[1])
        start_id = index.ntotal
        index.add(embeddings)
        faiss.write_index(index, INDEX_PATH)

        if os.path.exists(METADATA_PATH):
            meta = list(np.load(METADATA_PATH, allow_pickle=True))
        else:
            meta = []
        for i, chunk in enumerate(chunks):
            meta.append({
                "id": start_id + i,
                "text": chunk,
                "country": country,
                "source": file.filename
            })
        np.save(METADATA_PATH, np.array(meta, dtype=object))

        return {"message": f"PDF '{file.filename}' processed", "chunks": len(chunks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
