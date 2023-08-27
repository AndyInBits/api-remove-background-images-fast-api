from core.config import settings
from fastapi.encoders import jsonable_encoder
from jwt import decode, encode
from models.users import User as UserModel


def create_token(user: UserModel, secret: str = settings.SECRET_KEY) -> str:
    token: str = encode(jsonable_encoder(user), secret, algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    try:
        return decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except:
        return {}
