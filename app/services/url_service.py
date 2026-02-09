from sqlalchemy.orm import Session

from app.models.url import UrlMapping
from app.services.id_generator import generator
from app.utils.base62 import encode
from app.core.redis import redis_client
from app.core.bloom_filter import add_code, exists


BASE_URL = "http://localhost:8000"
TTL = 7 * 24 * 60 * 60

def _cache_key(short_code: str) -> str:
    return f"url:{short_code}"

def create_short_url(db: Session, long_url: str) -> str:
    snowflake_id = generator.generate_id()
    short_code = encode(snowflake_id)

    record = UrlMapping(
        id=snowflake_id,
        short_code=short_code,
        long_url=long_url
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    add_code(short_code)

    try:
        redis_client.set(
            _cache_key(short_code),
            long_url,
            ex=TTL
        )
    except Exception:
        pass

    return f"{BASE_URL}/{short_code}"


def get_long_url(db: Session, short_code: str) -> str | None:
    
    if not exists(short_code):
        return None
    try:
        cached = redis_client.get(_cache_key(short_code))
        if cached:
            return cached
    except Exception:
        pass
    record = (
        db.query(UrlMapping)
        .filter(UrlMapping.short_code == short_code)
        .first()
    )
    if not record:
        return None
    
    try:
        redis_client.set(
            _cache_key(short_code), 
            record.long_url, 
            ex=TTL
        )
    except Exception:
        pass
    return record.long_url
