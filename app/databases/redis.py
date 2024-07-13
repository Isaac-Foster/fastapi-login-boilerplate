import redis

from fastapi import Request
from functools import wraps
from typing import Callable


class RedisManager(redis.Redis):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def insert(self, key: str, value: str | int, time: int):
        """
        This funcions is used for created insert using TTL data
        arg: value is seconds
        """
        self.setex(
            name=str(key),
            time=time,
            value=value
        )
    
    def search(self, key: str):
        if self.get(key):
            return self.get(key).decode("utf8")
        return self.get(key)    


redis_manager = RedisManager(host="localhost", port=6379, db=0)

def login_required(f: Callable):
    @wraps(f)
    async def main(*args, **kwargs):
        request: Request = kwargs.get("request")
        session_id = request.cookies.get("session")
        if session_id and redis_manager.search(session_id):
            return await f(*args, **kwargs)
        return dict(message="fazer login")
    return main
