from pyrogram import Client

from app.data import Config

import logging

logging.basicConfig(
    level=logging.INFO,
    filename='log.log',
    filemode='w',
    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(name)s] [%(filename)s:%(lineno)d] %(message)s'
)

logging.getLogger('youtube_dl').setLevel(logging.ERROR)
logging.getLogger('pyrogram.session.session').setLevel(logging.CRITICAL)
logging.getLogger('pyrogram.connection.connection').setLevel(logging.CRITICAL)
logging.getLogger('pyrogram.dispatcher').setLevel(logging.ERROR)


plugins = dict(root="app.handlers")

client: Client = Client(
    name="client",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins
)

client.desc = {}

