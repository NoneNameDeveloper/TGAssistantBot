from pyrogram import Client, filters, types

from loader import client


@Client.on_message(filters.me & filters.regex("^\.purge"))
async def purge(client: Client, message: types.Message):
    """purge self messages from chat"""
    count = message.text[7:]

    if not count or not count.isdigit():
        return await message.edit("Provide an integer count of messages to remove.")

    count = int(count)

    pro_count = 0

    await message.edit("🧹 <b>Purging started...</b>")
    status_msg_id = message.id

    async for msg in client.get_chat_history(message.chat.id):
        if msg.from_user and msg.from_user.id == message.from_user.id and msg.id != status_msg_id:
            await msg.delete()

            pro_count += 1

            if pro_count >= count:
                return await message.edit(f"<b>✅ Purging finished.</b> Purged messages count: {pro_count}.")

    return await message.edit(f"<b>✅ Purging finished.</b> Purged messages count: {pro_count}.")


client.desc['Purge'] = {
    "use": ".purge <count>",
    "description": "Purge provided count of your messages from current chat."
}
