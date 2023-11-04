import os.path

from pyrogram import types, Client

from pyrogram import filters

from loader import client


@Client.on_message(filters.me & filters.text & filters.regex("^\.log"))
async def log(client: Client, message: types.Message):
    """get program log"""
    if os.path.exists("log.log"):
        with open("log.log", "rb") as f:
            await client.send_document("me", document=f)

            return await message.edit("Logs was exported!")

client.desc["Log Export"] = {
    "use": ".log",
    "description": "Export app logs to \"Saved Messages\"."
}