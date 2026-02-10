import os

class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://url_user:url_pass@postgres:5432/url_shortener"
    )
    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://redis:6379"
    )

settings = Settings()