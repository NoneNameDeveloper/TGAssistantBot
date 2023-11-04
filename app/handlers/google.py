from pyrogram import types, Client

from pyrogram import filters

from app.filters import is_admin

import urllib.parse

from loader import client

g_link = "https://www.google.com/search?q="


@Client.on_message(is_admin & filters.text & filters.regex("^\.g"))
async def google(client: Client, message: types.Message):
    """print sentence letter by letter"""
    text_splitted = message.text[3:]

    await message.edit(
        (g_link + urllib.parse.quote_plus(text_splitted)), disable_web_page_preview=True
    )

client.desc["Google Search"] = {
    "use": ".g {query}",
    "description": "Getting url-encoded google search url for given query."
}