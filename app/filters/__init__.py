from .is_admin import is_admin_filter
from .text_equals import text_equals
from .is_dmuted import is_dmuted

from pyrogram import filters

is_admin = filters.create(is_admin_filter)
is_dmuted = filters.create(is_dmuted)
