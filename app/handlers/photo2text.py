from PIL import Image
import pytesseract

import os

from pyrogram import types, Client

from pyrogram import filters

from app.data import Config
from app.engine.utils import get_timestamp

from app.filters import is_admin

import html

from loader import client


@Client.on_message(is_admin & filters.text & filters.regex("^\.pt$") &
                   filters.reply)
async def voice2text(client: Client, message: types.Message):
    """extract text from photo"""
    if not message.reply_to_message.photo:
        return

    file_name: str = get_timestamp() + ".jpg"
    file_path: str = Config.PHOTO_STORAGE + file_name

    await message.reply_to_message.download(file_path)

    await message.edit("<b>Processing...</b>")

    image = Image.open(file_path)

    text = pytesseract.image_to_string(image, lang="rus")

    os.remove(file_path)

    return await message.edit(f"<b>🪄 Extracted text: </b>\n{html.escape(text)}")


client.desc["Photo2Text"] = {
    "use": ".pt (Reply)",
    "description": "Extract text from photo (RU language)"
}