from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import init_db, SessionLocal
from app.core.redis import init_redis
from app.core.bloom_filter import load_existing_codes
from app.api.routes.url import router as url_router



@asynccontextmanager
async def lifespan(app:FastAPI):
    # Startup
    init_db()
    init_redis()
    db = SessionLocal()
    try:
        load_existing_codes(db)
    finally:
        db.close()
    yield
    # Shutdown (to-do)



app = FastAPI(
    title="Distributed URL shortener",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(url_router)