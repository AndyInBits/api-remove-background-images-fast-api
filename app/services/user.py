import base64
import hashlib
from db.session import Session

from fastapi import HTTPException
from jwt_manager.jwt_manager import create_token, validate_token
from models.users import User as UserModel
from schemas.user import User, UserAuth, UserEdit, UserLogin
from redis_config.config import RedisInstance


class UserService:
    def __init__(self) -> None:
        self.db = Session()
        self.redis = RedisInstance()

    def create_user(self, user: User) -> UserAuth:
        user.password = self.password_hash(user.password)

        new_user = UserModel(
            email=user.email,
            password=user.password,
            full_name=user.full_name,
        )
        self.db.add(new_user)
        self.db.commit()
        user = (
            self.db.query(UserModel).filter(UserModel.email == new_user.email).first()
        )
        token = create_token(user)
        response = UserAuth(email=user.email, token=token)
        self.db.close()
        return response

    def update_user(self, user_param: User, token: str) -> User:
        data = validate_token(token)
        user = self.db.query(UserModel).filter(UserModel.id == data["id"]).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.email = user_param.email
        user.full_name = user_param.full_name
        self.db.commit()
        self.db.refresh(user)
        self.db.close()
        response = UserEdit(email=user.email, full_name=user.full_name)
        return response

    def delete_user(self, token: str) -> None:
        data = validate_token(token)
        user = self.db.query(UserModel).filter(UserModel.id == data["id"]).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        self.db.delete(user)
        self.db.commit()
        self.db.close()

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

        self.redis.set_data(user.email, response.token)
        return response

    def password_hash(self, password: str) -> str:
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode("utf-8"))
        hash_value = sha256_hash.digest()
        base64_encoded = base64.b64encode(hash_value)
        base64_hash = base64_encoded.decode("utf-8")

        return base64_hash
