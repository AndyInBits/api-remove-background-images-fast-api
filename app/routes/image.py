from fastapi import APIRouter, Depends, Header, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer
from models.images import Image as ImageModel
from schemas.image import Image, ImageResponse
from services.image import ImageService


def get_jwt_token(authorization: str = Header(...)):
    return authorization.split("Bearer ")[1]

images_router = APIRouter()
 
@images_router.post("/process_images", tags=["Images"], dependencies=[Depends(JWTBearer())], response_model=ImageResponse)
async def handler_image(request: Request, image: Image = Depends()) -> ImageResponse:
    jwt = get_jwt_token(request.headers.get("authorization"))
    response = ImageService().handler_image(image, token=jwt)
    return JSONResponse(status_code=200, content=jsonable_encoder(response))

@images_router.get("/my_images", tags=["Images"], dependencies=[Depends(JWTBearer())])
async def handler_image(request: Request) -> list[ImageResponse]:
    jwt = get_jwt_token(request.headers.get("authorization"))
    response = ImageService().get_all_images_from_user(jwt=jwt)
    return JSONResponse(status_code=200, content=jsonable_encoder(response))

@images_router.delete("/delete_image/{id}", tags=["Images"], dependencies=[Depends(JWTBearer())])
async def handler_image(request: Request, id) -> list[ImageResponse]:
    jwt = get_jwt_token(request.headers.get("authorization"))
    ImageService().delete_image_from_user(jwt=jwt, img_id=id)
    return JSONResponse(status_code=200, content="OK")