import datetime

from pyrogram import types, Client

from pyrogram import filters

from loader import client


@Client.on_message(filters.me & filters.text & filters.regex("^\.ping$"))
async def ping(client: Client, message: types.Message):
    """ping from server"""
    now = datetime.datetime.now()
    m = await message.edit("<b>🏓 Ping</b>")
    end = datetime.datetime.now()
    await m.edit(f"<b>🏓 Pong:</b> {(now-end).microseconds / 1000} ms.")

client.desc["Ping"] = {
    "use": ".ping",
    "description": "Get ping time from server."
}