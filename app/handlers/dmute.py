from pyrogram import types, Client

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatMember

from app.engine.storage.redis_service import get_dmute, add_dmute, remove_dmute

import logging

from app.filters import is_dmuted
from loader import client


@Client.on_message(filters.group & filters.me & filters.text & filters.regex("^\.dmute"))
async def dmute(client: Client, message: types.Message):
    """delete all messages from user"""
    usr: ChatMember = await client.get_chat_member(message.chat.id, message.from_user.id)

    if not usr.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await message.edit("Not enough permissions :(")

    if message.reply_to_message:
        target_id = message.reply_to_message.from_user.id

        dmute_list = await get_dmute()

        target_full_name = message.reply_to_message.from_user.first_name or "" + message.reply_to_message.from_user.last_name or ""

        if target_id in dmute_list:
            return await message.edit(f"<b>{target_full_name}</b> already in dmute.")

        await add_dmute(target_id)

        logging.debug(f"{target_id} added to dmute.")

        await message.edit(f"<b>{target_full_name}</b> was dmuted!")


@Client.on_message(filters.group & filters.me & filters.text & filters.regex("^\.undmute"))
async def undmute(client: Client, message: types.Message):
    """delete all messages from user"""

    if message.reply_to_message:
        target_id = message.reply_to_message.from_user.id

        dmute_list = await get_dmute()

        target_full_name = message.reply_to_message.from_user.first_name or "" + message.reply_to_message.from_user.last_name or ""

        if target_id not in dmute_list:
            return await message.edit(f"<b>{target_full_name}</b> not in dmute.")

        await remove_dmute(target_id)

        logging.debug(f"{target_id} removed from dmute.")

        await message.edit(f"<b>{target_full_name}</b> was undmuted!")


@Client.on_message(filters.group & is_dmuted)
async def dmute_del(client: Client, message: types.Message):
    try:
        await message.delete()
    except Exception as e:
        logging.error(e)


client.desc["Del Mute"] = {
    "use": ".dmute (Reply)",
    "description": "Delete all messages from user, while in dmute."
}

client.desc["UnDel Mute"] = {
    "use": ".undmute (Reply)",
    "description": "UnDmute user."
}
