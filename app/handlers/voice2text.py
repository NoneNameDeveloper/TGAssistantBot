import logging
import os

from pyrogram import types, Client

from pyrogram import filters

from app.data import Config
from app.engine.utils import get_timestamp

import openai

from loader import client


async def process_downloading(current, total, message):
    await message.edit(f"<b>Downloading</b> {current/total*100}%")


@Client.on_message(filters.me & filters.text & filters.regex("^\.vt$") &
                   filters.reply)
async def voice2text(client: Client, message: types.Message):
    """transcribe voice to text"""
    if not message.reply_to_message.voice:
        return await message.edit("<b>This is not a voice..</b>")

    if not Config.OPENAI_KEY:
        return await message.edit("There is an error, check <code>.log</code> for details..")

    file_name: str = get_timestamp() + ".ogg"
    file_path: str = Config.VOICE_STORAGE + file_name

    await message.reply_to_message.download(file_path, progress=process_downloading,
                                            progress_args=(message,))

    try:
        with open(file_path, "rb") as audio_file:
            transcript = openai.OpenAI(api_key=Config.OPENAI_KEY).audio.translations.create(
                file=audio_file, model="whisper-1"
            ).text
    except Exception as e:
        logging.error(e)
        return await message.edit("Can't transcribe this ;(")

    os.remove(file_path)

    if transcript.strip() != "":

        return await message.edit(transcript)
    else:
        return await message.edit("Can't transcribe this ;(")

client.desc["Voice2Text"] = {
    "use": ".vt (Reply)",
    "description": "Transcribe voice message to text, using Whisper."
}