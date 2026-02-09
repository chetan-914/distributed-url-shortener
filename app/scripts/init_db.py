from sqlalchemy import create_engine
from app.models.base import Base
from app.models.url import UrlMapping

engine = create_engine("postgresql://url_user:url_pass@localhost:5432/url_shortener")

Base.metadata.create_all(bind=engine)