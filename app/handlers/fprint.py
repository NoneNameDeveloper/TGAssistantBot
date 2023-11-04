from pyrogram import types, Client

from pyrogram import filters

from app.filters import is_admin
from loader import client


@Client.on_message(is_admin & filters.text & filters.regex("^\.fprint"))
async def fprint(client: Client, message: types.Message):
    """print sentence letter by letter"""

    text_splitted = message.text.split()

    if len(text_splitted) < 2:
        return

    f_text = " ".join(text_splitted[1:])

    r_string = ""

    for i in range(len(f_text)):
        r_string += f_text[i]
        if i != len(f_text) - 1:
            await message.edit(r_string + "...")
        else:
            await message.edit(r_string)

client.desc["Fuck Print"] = {
    "use": ".fprint {query}",
    "description": "Write given query letter by letter"
}