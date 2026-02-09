from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models.base import Base

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True, pool_recycle=300)

SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)

def init_db():
    with engine.connect() as conn:
        pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
