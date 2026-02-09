import redis
from app.core.config import settings

redis_client = None

def init_redis():
    global redis_client
    redis_client = redis.Redis.from_url(
        settings.REDIS_URL
    )
    redis_client.ping()