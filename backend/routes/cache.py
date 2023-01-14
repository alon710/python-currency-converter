import os

from cachetools import TTLCache


def get_cache() -> TTLCache:
    return TTLCache(
        maxsize=int(
            os.getenv("TTL_MAX_SIZE"),
        ),
        ttl=int(
            os.getenv("TTL_TIME_IN_SEC"),
        ),
    )


cache = get_cache()
