from pyrogram import filters
from app.data import Config


def text_equals(data):
    async def process(flt, __, query):
        """check if text on equals"""
        return flt.data == query.text

    return filters.create(process, data=data)
