import html
import io
import logging
import os

from openai import OpenAI
from pyrogram import types, Client

from pyrogram import filters

from app.data import Config
from app.engine.utils import get_timestamp


from loader import client


def tts(text, model, voice) -> io.BytesIO | None:

    try:
        client = OpenAI(api_key=Config.OPENAI_KEY)

        response = client.audio.speech.create(
            model=model,  # "tts-1","tts-1-hd"
            voice=voice,  # 'alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'
            input=text,
            response_format="mp3"
        )
        return io.BytesIO(response.content)

    except Exception as error:
        logging.error(f"An error occurred while generating speech: {error}")
        return None


@Client.on_message(filters.me & filters.text & filters.regex("^\.tv"))
async def voice2text(client: Client, message: types.Message):
    """transcribe text to voice"""
    if message.reply_to_message:
        if message.reply_to_message.text or message.reply_to_message.caption:
            text_to_translate = message.reply_to_message.caption or message.reply_to_message.text
        else:
            text_to_translate = message.text[4:]
    else:
        text_to_translate = message.text[4:]

    if not text_to_translate:
        return await message.edit("Data to TTS is empty!")

    if not Config.OPENAI_KEY:
        return await message.edit("There is an error, check <code>.log</code> for details..")

    await message.edit("Processing...Wait for a 3-5 sec...")

    res = tts(text_to_translate, "tts-1", "shimmer")

    if not res:
        return await message.edit("Sorry, I couldn't process it :(")

    await message.delete()

    res.name = "tts.mp3"

    await client.send_voice(
        message.chat.id,
        voice=res,
        caption="<code>" + html.escape(text_to_translate) + "</code>",
    )


client.desc["Text2Voice"] = {
    "use": ".tv (Reply/Text)",
    "description": "Translating text to voices"
}