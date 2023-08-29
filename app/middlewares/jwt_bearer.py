from db.session import Session
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from jwt_manager.jwt_manager import validate_token
from models.users import User as UserModel
from redis_config.config import RedisInstance


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        redis = RedisInstance()
        if not redis.get_data(data["email"] ):
            db = Session()
            user = db.query(UserModel).filter(UserModel.id == data["id"]).first()
            db.close()
            if not user:
                raise HTTPException(status_code=403, detail="Forbidden")
