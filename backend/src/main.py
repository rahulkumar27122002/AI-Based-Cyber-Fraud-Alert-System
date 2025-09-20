# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from motor.motor_asyncio import AsyncIOMotorClient  # 👈 use Mongo instead of psycopg2

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development allow all. Restrict later e.g. ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- MongoDB ----------------
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/mydb")

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(MONGO_URL)
    app.database = app.mongodb_client.get_default_database()

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

# ---------------- Routes ----------------
@app.get("/")
async def root():
    return {"message": "Backend is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/health/db")
async def health_db():
    try:
        pong = await app.database.command("ping")
        if pong.get("ok") == 1:
            return {"db": "ok"}
        raise HTTPException(status_code=500, detail="db ping failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
