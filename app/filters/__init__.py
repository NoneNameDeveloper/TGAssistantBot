from .text_equals import text_equals
from .is_dmuted import is_dmuted

from pyrogram import filters

is_dmuted = filters.create(is_dmuted)
