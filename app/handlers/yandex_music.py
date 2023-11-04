import asyncio
import logging
import os
import re
from typing import Iterator

from pyrogram import Client, filters

from pyrogram.types import Message

import youtube_dl

from app.data import Config

from loader import client

ydl_options = {
    'outtmpl': os.path.abspath(Config.VOICE_STORAGE + "/%(title)s.%(ext)s"),
    'cookiefile': os.path.abspath("app/data/cookies"),
    'quiet': True
}

ydl = youtube_dl.YoutubeDL(params=ydl_options)

tracks_path = os.path.abspath(Config.VOICE_STORAGE)


async def ymusic_download(music_link: str) -> Iterator[dict | str]:
    """download and return path"""
    if not re.match(r"https://music.yandex.ru/album/(.*)/track/(.*)", music_link):
        yield {"error": "Provided url is not valid track :("}

    try:
        a = await asyncio.to_thread(ydl.extract_info, music_link, False)

        title = a['title']
        ext = a['ext']
        # print(a)
        yield {"info": f"<b>🎸 Track Title:</b> <code>{title}</code>. Downloading..."}

        await asyncio.to_thread(ydl.download, [music_link])
        yield {"info": f"<b>📧 Sending track...</b>"}

        yield tracks_path + f"/{title}.{ext}"

    except Exception as e:
        logging.error(e)
        yield {"error": e}


@Client.on_message(filters.me & filters.regex("^\.ym"))
async def yamusic(client: Client, message: Message):
    """download music from yandex by link"""
    music_link = message.text[4:]

    future = ymusic_download(music_link)

    async for r in future:
        if isinstance(r, dict):
            if r.get("error"):
                return await message.edit(r.get("error"))
            elif r.get("info"):
                await message.edit(r.get("info"))

        if isinstance(r, str):
            await message.delete()

            await client.send_audio(
                message.chat.id,
                audio=r
            )

            os.remove(r)


client.desc["Yandex Music Download"] = {
    "use": ".ym <link>",
    "description": "Download provided track from Y Music."
}