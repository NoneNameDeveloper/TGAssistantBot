# <p align="center">🤖 TGAssistantBot</p>

<hr>

## 📜 Installation
```bash
git clone https://github.com/NoneNameDeveloper/TGAssistantBot
```
```bash
cd TGAssistantBot
```
```bash
cp .env.example .env
```
Fill .env file with your data.
1. Follow https://my.telegram.org to get `API_ID` and `API_HASH`
2. Fill `REDIS_HOST` and `REDIS_PORT` to access Redis storage
3. Fill `OPENAI_KEY` to access voice to text function
4. Create file /app/data/cookies with cookies in the *netscape* format from music.yandex.ru to download full versions of tracks, using `.ym <track_link>`

```bash
python3 main.py
```
Authorize to telegram account with Phone number and code (if you are logging in first time)


## 🧑‍💻 Modules
You can write your own modules and load them dynamically, using `.dlmod` command.

Example of extra module:
```python
import logging

from pyrogram import types, Client

from pyrogram import filters

from loader import client


@Client.on_message(filters.me & filters.text & filters.reply & filters.regex("^\.d$"))
async def delete(client: Client, message: types.Message):
    """delete replied message"""
    try:
        await message.reply_to_message.delete()

        await message.delete()
    except Exception as e:
        logging.error(e)
        return await message.edit(f"Error: <code>e</code>")

client.desc["Delete"] = {
    "use": ".d <reply>",
    "description": "Deletet replied message."
}
```

If you are using extra packages in your module, you can install them using `.term pip install <module-name>`
