from db.session import Session
from jwt_manager.jwt_manager import validate_token
from fastapi.security import HTTPBearer
from fastapi import HTTPException, Request
from models.users import User as UserModel

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        db = Session()
        user = db.query(UserModel).filter(UserModel.id == data["id"]).first()
        db.close()
        if not user:
            raise HTTPException(status_code=403, detail="Forbidden")
