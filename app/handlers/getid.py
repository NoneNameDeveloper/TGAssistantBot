from pyrogram import types, Client

from pyrogram import filters

from loader import client


@Client.on_message(filters.me & filters.text & filters.regex("^\.id$"))
async def getid(client: Client, message: types.Message):
    """ping from server"""

    if not message.reply_to_message:
        return await message.edit(
            f"Chat Id: {message.chat.id}"
        )

    else:
        return await message.edit(
            f"Chat Id: <code>{message.chat.id}</code>\n"
            f"User Id: <code>{message.reply_to_message.from_user.id}</code>"
        )

client.desc["Get ID"] = {
    "use": ".id",
    "description": "Getting id of current chat. (Can use with reply)."
}