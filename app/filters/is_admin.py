from app.data import Config


async def is_admin_filter(_, __, query):
    """check if message sent by owner"""
    if query.from_user:
        return str(query.from_user.id) == str(Config.ADMIN_ID)
