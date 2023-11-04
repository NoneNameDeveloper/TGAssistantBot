import time


def get_timestamp() -> str:
    """get unique string as timestamp value"""
    return str(int(time.time()))

