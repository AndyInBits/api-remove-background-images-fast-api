from core.config import settings
from fastapi.encoders import jsonable_encoder
from jwt import decode, encode
from models.users import User as UserModel
from fastapi import HTTPException


def create_token(user: UserModel, secret: str = settings.SECRET_KEY) -> str:
    token: str = encode(jsonable_encoder(user), secret, algorithm="HS256")
    return token


def validate_token(token: str, secret: str = settings.SECRET_KEY) -> dict:
    try:
        token = decode(token, secret, algorithms=["HS256"])
        if not token:
            raise HTTPException(403, detail="User not authenticated")
        return token

    except:
        raise HTTPException(403, detail="User not authenticated")
