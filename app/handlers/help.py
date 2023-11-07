from pyrogram import types, Client

from pyrogram import filters


@Client.on_message(filters.me & filters.text & filters.regex("^\.help$"))
async def help(client: Client, message: types.Message):
    """return modules list and help FAQ"""
    await message.edit(
        "\n".join(f"<b>· {title}</b>\n{use['use']} <i>({use['description']})</i>" for title, use in client.desc.items() if list(use.keys()) == ['use', 'description']) + "\n\n<b>🗂 Repository: <a href='https://github.com/NoneNameDeveloper/TGAssistantBot'>click</a></b>",
        disable_web_page_preview=True
    )
