import aioredis
from aioredis import from_url
from app.core.config import settings

redis = None


async def init_redis():
    redis = await from_url(settings.redis.url, encoding="utf-8", decode_responses=True)
    return redis


async def close_redis():
    await redis.close()
