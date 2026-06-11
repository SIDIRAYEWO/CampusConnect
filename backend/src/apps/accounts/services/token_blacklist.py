import redis

from django.conf import settings


redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True,
)


def blacklist_token(jti: str, ttl: int):
    redis_client.setex(
        f"blacklist:{jti}",
        ttl,
        "revoked"
    )


def is_token_blacklisted(jti: str) -> bool:
    return redis_client.exists(
        f"blacklist:{jti}"
    ) == 1