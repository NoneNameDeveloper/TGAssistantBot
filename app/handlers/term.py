import asyncio

from pyrogram import types, Client

from pyrogram import filters

import logging

from loader import client

import subprocess


@Client.on_message(filters.me & filters.text & filters.regex("^\.term"))
async def term(_, message: types.Message):
    splitted_text = message.text[6:]

    try:
        a = await asyncio.to_thread(
            subprocess.run,
            args=splitted_text,
            stdout=subprocess.PIPE,
            shell=True,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        logging.error(e)
        return await message.edit(f"<b>Error:</b> {e}")

    await message.edit(
        f"<code>{splitted_text}</code> <b>output</b>:\n\n"
        f"<i>{a.stdout.decode('utf-8')}</i>"
    )


client.desc["Terminal"] = {
    "use": ".term <query>",
    "description": "Execute provided command in terminal."
}