from core.config import settings
from jwt import decode, encode


def create_token(data: dict, secret: str = settings.SECRET_KEY) -> str:
    token: str = encode(data, secret, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    try:
        return decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except:
        return {}
