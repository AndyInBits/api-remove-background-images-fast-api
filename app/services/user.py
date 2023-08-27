import base64
import hashlib

from core.config import settings
from fastapi import HTTPException
from jwt_manager.jwt_manager import create_token
from models.users import User as UserModel
from passlib.context import CryptContext
from schemas.user import User, UserAuth, UserEdit, UserLogin


class UserService:
    def __init__(self, db) -> None:
        self.db = db

    def create_user(self, user: User) -> UserAuth:
        user.password = self.password_hash(user.password)

        new_user = UserModel(
            email=user.email,
            password=user.password,
            full_name=user.full_name,
        )
        self.db.add(new_user)
        self.db.commit()
        token = create_token(new_user)
        response = UserAuth(email=new_user.email, token=token)
        self.db.close()
        return response
    
    def update_user(self, user_param: User, id: int) -> User:
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.email = user_param.email
        user.full_name = user_param.full_name
        self.db.commit()
        self.db.refresh(user)
        self.db.close()
        response = UserEdit(email=user.email, full_name=user.full_name)
        return response
    
    def delete_user(self, id: int) -> None:
        user = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        self.db.delete(user)
        self.db.commit()
        self.db.close()
        return None

    def login_user(self, user_param: UserLogin) -> UserAuth:
        user = (
            self.db.query(UserModel).filter(UserModel.email == user_param.email).first()
        )
        self.db.close()

        if not user:
            raise HTTPException(
                status_code=400, detail="Incorrect username or password"
            )

        if not user.password == self.password_hash(user_param.password):
            raise HTTPException(
                status_code=400, detail="Incorrect username or password"
            )
        response = UserAuth(email=user.email, token=create_token(user))
        return response

    def password_hash(self, password: str) -> str:
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode("utf-8"))
        hash_value = sha256_hash.digest()
        base64_encoded = base64.b64encode(hash_value)
        base64_hash = base64_encoded.decode("utf-8")

        return base64_hash
