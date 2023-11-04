import redis.asyncio as redis

from app.data import Config

import logging

client: redis.Redis | None = None


async def init_redis_storage():
    global client

    logging.info("Redis storage initialised")

    client = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)


async def add_dmute(user_id: str):
    await client.lpush("dmute", user_id)


async def remove_dmute(user_id: str):
    await client.lrem("dmute", 1, user_id)


async def get_dmute() -> list:

    res = []
    for i in range(await client.llen("dmute")):
        res.append(int(await client.lindex("dmute", i)))

    return res
