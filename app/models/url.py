from sqlalchemy import Column, String, DateTime, BigInteger, func
from app.models.base import Base


class UrlMapping(Base):
    __tablename__ = "url_mapping"
    
    id = Column(BigInteger, primary_key=True, index=True)
    short_code = Column(String, index=True, unique=True, nullable=False)
    long_url = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)