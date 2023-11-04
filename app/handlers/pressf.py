from pyrogram import types, Client

from pyrogram import filters

from loader import client


@Client.on_message(filters.me & filters.text & filters.regex("^\.pressf"))
async def pressf(client: Client, message: types.Message):
    """print sentence letter by letter"""
    paytext = message.text[8:]

    f_text = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)

    await message.edit(f_text)
    
client.desc["Press F"] = {
    "use": ".pressf {f symbol}",
    "description": "Pressing F in symbol style."
}