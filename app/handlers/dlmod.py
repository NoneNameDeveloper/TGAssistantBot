import importlib.util
import inspect
import logging

import random
import string

import requests
from pyrogram import types, Client

from pyrogram import filters

from loader import client

from app.data import Config

import importlib


@Client.on_message(filters.me & filters.regex("^\.dlmod"))
async def dlmod(_, message: types.Message):
    splitted_text = message.caption[6:] if message.document else message.text[6:]

    # link provided
    if len(splitted_text) > 5:

        file_name = "".join([random.choice(string.ascii_letters) for _ in range(10)]) + ".py"

        logging.info(f".dlmod executed with url: {splitted_text}")
        file_path = Config.MODULES_STORAGE + file_name

        with open(file_path, "wb") as f:
            f.write(requests.get(splitted_text).content)

    # module provided
    elif message.document:

        file_name = message.document.file_name

        logging.info(f".dlmod executed with document: {file_name}")

        if not file_name.endswith(".py"):
            return await message.edit("File must be a .py file!")

        file_path = Config.MODULES_STORAGE + file_name

        await message.download(file_name=file_path)

    else:
        return

    await message.edit("Downloaded...")

    # path to downloaded file
    module_path = Config.MODULES_STORAGE + file_name

    # module name in memory
    module_name = file_name[:3]

    # Загрузка модуля
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(module)
    except Exception as e:
        logging.error(e)
        return await message.edit("<b>Failes to load module</b>.\n"
                                  f"Error: <code>{e}</code>")

    # getting function (under-handler) name, to add handler
    custom_handler = None
    for name, obj in module.__dict__.items():
        if callable(obj) and hasattr(obj, "__module__") and obj.__module__ == module_name:
            source = inspect.getsource(obj)
            if "@Client.on_message(" in source:
                custom_handler = obj
                break

    if not custom_handler:
        return await message.edit("<b>Failes to load module</b>.\n"
                                  f"Error: <code>Unable to load under-handler function name.</code>")

    for h in custom_handler.handlers:
        client.add_handler(*h)

    logging.info("Module loaded successfully!")
    return await message.edit("Module loaded successfully!")


client.desc["Download Module"] = {
    "use": ".dlmod <link to raw (optional)> / <.py document>",
    "description": "Download provided module."
}