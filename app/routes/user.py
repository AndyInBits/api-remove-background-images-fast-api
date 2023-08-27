from services.user import UserService
from db.session import Session
from schemas.user import User, UserAuth
from fastapi import APIRouter, Depends, Path, Query, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

user_router = APIRouter()


@user_router.post(
    "/user", tags=["Users"], response_model=UserAuth, status_code=200
)
def create_user(user: User = Body(...)) -> UserAuth:
    db = Session()
    response = UserService(db).create_user(user)
    return JSONResponse(content=jsonable_encoder(response), status_code=200)
