from typing import Optional

from db.session import Session
from models.users import User as UserModel
from pydantic import BaseModel, EmailStr, validator


class User(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    password: str
    password_confirmation: str
    full_name: str

    @validator("password_confirmation")
    def passwords_match_validate(cls, value, values, **kwargs):
        if "password" in values and value != values["password"]:
            raise ValueError("Password confirmation does not match password")
        return value
    
    @validator("email")
    def email_unique_validate(cls, value, values, **kwargs):
        db = Session()
        res = db.query(UserModel).filter(UserModel.email == value).all()
        db.close()
        if res:
            raise ValueError('Email must be unique!')
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "email": "admin@gmail.com",
                "password": "MySuperSecretPassword",
                "password_confirmation": "MySuperSecretPassword",
                "full_name": "John Doe",
            }
        }

    

class UserLogin(BaseModel):
    email: str
    password: str
   
    class Config:
        json_schema_extra = {
            "example": {
                "email": "admin@gmail.com",
                "password": "MySuperSecretPassword",
            }
        }

class UserAuth(BaseModel):
    token: str 
    email: str

class UserEdit(BaseModel):
    email: str
    full_name: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "new_admin@gmail.com",
                "full_name": "New name",
            }
        }