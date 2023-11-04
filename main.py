import logging

import asyncio
import os.path

from app.data import Config

from app.engine.storage.redis_service import init_redis_storage
from loader import client


async def main():
    await init_redis_storage()

    if not os.path.exists(Config.VOICE_STORAGE):
        logging.debug("Created voice storage")
        os.mkdir(Config.VOICE_STORAGE)

    if not os.path.exists(Config.PHOTO_STORAGE):
        logging.debug("Created photo storage")
        os.mkdir(Config.PHOTO_STORAGE)

    if not os.path.exists(Config.MODULES_STORAGE):
        logging.debug("Created modules storage")
        os.mkdir(Config.MODULES_STORAGE)

    if not os.path.exists(Config.MODULES_STORAGE + "/__init__.py"):
        logging.debug("Created module from modules storage")
        open(Config.MODULES_STORAGE + "/__init__.py", "w")

    logging.info("Client starting")


asyncio.get_event_loop().create_task(main())

client.run()
