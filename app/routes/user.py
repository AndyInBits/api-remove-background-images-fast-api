from db.session import Session
from fastapi import APIRouter, Body, Depends, Path, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.user import User, UserAuth, UserEdit, UserLogin
from services.user import UserService
from models.users import User as UserModel
from middlewares.jwt_bearer import JWTBearer
user_router = APIRouter()


@user_router.post(
    "/users", tags=["Users"], response_model=UserAuth, status_code=200
)
def create_user(user: User = Body(...)) -> UserAuth:
    db = Session()
    response = UserService(db).create_user(user)
    return JSONResponse(content=jsonable_encoder(response), status_code=200)


@user_router.put("/user/{id}", tags=["Users"], response_model=UserEdit, dependencies=[Depends(JWTBearer())])
def update_user(id: int, user: UserEdit = Body(...)) -> UserEdit:
    db = Session()
    response = UserService(db).update_user(user, id)
    return JSONResponse(content=jsonable_encoder(response), status_code=200)


@user_router.post(
    "/login", tags=["Users"], response_model=UserAuth, status_code=200
)
def login_user(user: UserLogin = Body(...)) -> UserAuth:
    db = Session()
    response = UserService(db).login_user(user)
    return JSONResponse(content=jsonable_encoder(response), status_code=200)

