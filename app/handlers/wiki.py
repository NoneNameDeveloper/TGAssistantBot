from pyrogram import types, Client

import wikipedia

from pyrogram import filters

import logging

from loader import client


@Client.on_message(filters.me & filters.text & filters.regex("^\.wiki"))
async def wiki(_, message: types.Message):
    splitted_text = message.text[6:]

    wikipedia.set_lang("ru")
    try:
        a = wikipedia.summary(splitted_text)
    except Exception as e:
        logging.error(e)
        a = None
        
    if a:
        await message.edit(a)
    else:
        await message.edit(f"No results found for \"<code>{splitted_text}</code>\"")

client.desc["Wiki"] = {
    "use": ".wiki {query}",
    "description": "Get summary from wiki to given query."
}