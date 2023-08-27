from jwt_manager.jwt_manager import create_token
from schemas.user import User, UserAuth
from models.users import User as UserModel
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db) -> None:
        self.db = db

    def create_user(self, user: User) -> UserAuth:
            user.password = pwd_context.hash(user.password)

            new_user = UserModel(
                email=user.email,
                password=user.password,
                full_name=user.full_name,
            )
            self.db.add(new_user)
            self.db.commit()
            token = create_token(new_user)
            response = UserAuth(
                email=new_user.email,
                token=token
            )   
            self.db.close()
            return response