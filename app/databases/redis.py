import redis

from fastapi import Request
from functools import wraps
from typing import Callable

engine = redis.Redis(host="localhost", port=6379, db=0)


class RedisManager:
    engine = engine

    def __init__(self):
        pass

    def insert(self, key: str, value: str | int, time: int):
        """
        This funcions is used for created insert using TTL data
        arg: value is seconds
        """

        self.engine.setex(
            name=str(key),
            time=time,
            value=value
        )
    
    def get(self, key: str):
        if self.engine.get(key):
            return self.engine.get(key).decode("utf8")
        return self.engine.get(key)


redis_manager = RedisManager()

def login_requeried(f: Callable):
    @wraps(f)
    async def main(*args, **kwargs):
        request: Request = kwargs.get("request")
        session_id = request.cookies.get("session")
        if session_id and redis_manager.get(session_id):
            return await f(*args, **kwargs)
        return dict(message="fazer login")
    return main
