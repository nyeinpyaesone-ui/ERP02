import pickle
from typing import Any, Optional
import redis.asyncio as redis
from app.config import settings
import structlog

logger = structlog.get_logger()

class CacheManager:
    def __init__(self):
        self._redis: Optional[redis.Redis] = None

    async def connect(self):
        try:
            self._redis = redis.from_url(str(settings.REDIS_URL), decode_responses=False)
            await self._redis.ping()
            logger.info("cache_manager_connected")
        except Exception as e:
            logger.warning("cache_connection_failed", error=str(e))

    async def get(self, key: str) -> Optional[Any]:
        if not self._redis:
            return None
        try:
            data = await self._redis.get(key)
            return pickle.loads(data) if data else None
        except Exception:
            return None

    async def set(self, key: str, value: Any, ttl: int = None):
        if self._redis:
            try:
                ttl = ttl or settings.CACHE_DEFAULT_TTL
                await self._redis.setex(key, ttl, pickle.dumps(value))
            except Exception as e:
                logger.warning("cache_set_failed", error=str(e))

    async def delete(self, key: str):
        if self._redis:
            try:
                await self._redis.delete(key)
            except Exception:
                pass

    async def delete_pattern(self, pattern: str):
        if self._redis:
            try:
                keys = await self._redis.keys(pattern)
                if keys:
                    await self._redis.delete(*keys)
            except Exception:
                pass

    async def health(self):
        try:
            if self._redis:
                await self._redis.ping()
                return "connected"
        except Exception:
            pass
        return "disconnected"

    async def disconnect(self):
        if self._redis:
            await self._redis.close()

cache_manager = CacheManager()