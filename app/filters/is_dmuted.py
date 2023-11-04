from app.engine.storage.redis_service import get_dmute


async def is_dmuted(_, __, query):
    """check if user in dmutes list"""
    dmute_list = await get_dmute()

    if query.from_user:
        return query.from_user.id in dmute_list

