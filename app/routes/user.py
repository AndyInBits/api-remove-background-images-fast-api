from fastapi import APIRouter, Body, Depends,Request, Header
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.user import User, UserAuth, UserEdit, UserLogin
from services.user import UserService
from models.users import User as UserModel
from middlewares.jwt_bearer import JWTBearer
user_router = APIRouter()

def get_jwt_token(authorization: str = Header(...)):
    return authorization.split("Bearer ")[1]

@user_router.post(
    "/users", tags=["Users"], response_model=UserAuth, status_code=200
)
def create_user(user: User = Body(...)) -> UserAuth:
    response = UserService().create_user(user)
    return JSONResponse(content=jsonable_encoder(response), status_code=200)


@user_router.put("/user", tags=["Users"], response_model=UserEdit, dependencies=[Depends(JWTBearer())])
def update_user(request: Request, user: UserEdit = Body(...)) -> UserEdit:
    jwt = get_jwt_token(request.headers.get("authorization"))
    response = UserService().update_user(user, jwt)
    return JSONResponse(content=jsonable_encoder(response), status_code=200)

@user_router.delete("/user", tags=["Users"], response_model=dict,dependencies=[Depends(JWTBearer())])
def delete_user(request: Request) -> dict:
    jwt = get_jwt_token(request.headers.get("authorization"))
    UserService().delete_user(jwt)
    return JSONResponse(content={"msg": "User Deleted"}, status_code=200)

@user_router.post(
    "/login", tags=["Users"], response_model=UserAuth, status_code=200
)
def login_user(user: UserLogin = Body(...)) -> UserAuth:
    response = UserService().login_user(user)
    return JSONResponse(content=jsonable_encoder(response), status_code=200)

