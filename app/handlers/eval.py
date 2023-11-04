import logging
import traceback

from pyrogram import types, Client

from pyrogram import filters
import html

import os.path
import random
import string

import subprocess

from app.data import Config


def ceval(code: str) -> (str, str):
    """evaluate code"""
    file_name = "".join([random.choice(string.ascii_letters) for _ in range(10)]) + ".py"

    file_path = os.path.abspath(Config.CODES_STORAGE + "/" + file_name)

    with open(file_path, "w") as f:
        f.write(code)

    a = subprocess.Popen(
        ["python " + file_path],
        shell=True,
        stdin=None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    out, err = a.communicate()

    os.remove(file_path)

    return out.strip().decode("utf-8"), err.strip().decode("utf-8")


@Client.on_message(filters.me & filters.text & filters.regex("^\.eval"))
async def evals(client: Client, message: types.Message):
    """eval code"""
    text = message.text[6:]

    res = ceval(text)

    if not res[1]:
        await message.edit(f"<b>Code:</b>\n<code>{html.escape(text.lstrip())}</code>\n\n<b>Output:</b> \n" + f"<code>{html.escape(res[0])}</code>")
    else:
        await message.edit(f"<b>Code:</b>\n<code>{html.escape(text.lstrip())}</code>\n\n<b>Error:</b> \n" + f"<code>{html.escape(res[1])}</code>")

