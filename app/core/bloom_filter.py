from pybloom_live import BloomFilter
from sqlalchemy.orm import Session
from app.models.url import UrlMapping

BLOOM_CAPACITY = 10_000_000
BLOOM_ERROR_RATE = 0.001

bloom = BloomFilter(
    capacity=BLOOM_CAPACITY,
    error_rate=BLOOM_ERROR_RATE
)

def load_existing_codes(db: Session):
    records = db.query(UrlMapping.short_code).all()
    for (code,) in records:
        bloom.add(code)

def add_code(short_code: str):
    bloom.add(short_code)

def exists(short_code: str) -> bool:
    return short_code in bloom