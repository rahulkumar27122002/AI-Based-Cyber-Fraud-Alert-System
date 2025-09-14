# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import psycopg2  # add psycopg2-binary to requirements.txt

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development allow all. Restrict later e.g. ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Routes ----------------
@app.get("/")
async def root():
    return {"message": "Backend is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/health/db")
async def health_db():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise HTTPException(status_code=500, detail="DATABASE_URL not set")
    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            _ = cur.fetchone()
        conn.close()
        return {"db": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
