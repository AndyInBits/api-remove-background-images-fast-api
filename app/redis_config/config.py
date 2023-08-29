import redis
from core.config import settings


class RedisInstance:
    def __init__(self):
        self.redis = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)
    
    def get_data(self, key):
        return self.redis.get(key)

    def set_data(self, key, value):
        return self.redis.set(key, value)
