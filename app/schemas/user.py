from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    email: str
    password: str
    password_confirmation: str
    full_name: str


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