import logging

from dotenv import load_dotenv

import os


load_dotenv()


class Config:
    API_ID = os.getenv("API_ID")
    API_HASH = os.getenv("API_HASH")

    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")

    ADMIN_ID = os.getenv("OWN_ID")

    VOICE_STORAGE = "app/data/storage/"
    PHOTO_STORAGE = "app/data/photo/"

    MODULES_STORAGE = "app/handlers/custom_handlers/"

    CODES_STORAGE = "/tmp"

    OPENAI_KEY = os.getenv("OPENAI_KEY")

    # setting openai key to env
    if OPENAI_KEY:
        os.environ.setdefault("OPENAI_API_KEY", OPENAI_KEY)

    else:
        logging.warning("Openai key was not provided.")
