

from pyrogram import types, Client

from pyrogram import filters

from loader import client


@Client.on_message(filters.me & filters.text & filters.regex("^\.tagall"))
async def tagall(client: Client, message: types.Message):
    """tag all users in chat"""

    text_splitted = message.text.split()[1:]

    await message.edit("Processing...")
    sh = " ".join(text_splitted)
    if not sh:
        sh = "Hi!"

    mentions = ""
    async for member in client.get_chat_members(message.chat.id):
        mentions += member.user.mention + " "
    n = 4096
    kk = [mentions[i: i + n] for i in range(0, len(mentions), n)]
    for i in kk:
        j = f"<b>{sh}</b> \n{i}"
        await client.send_message(message.chat.id, j)


client.desc["Tag All"] = {
    "use": ".tagall <text>",
    "description": "Tag all users in chat"
}