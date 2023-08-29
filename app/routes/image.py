from services.image import ImageService
from schemas.image import Image
from models.images import Image as ImageModel
from fastapi import APIRouter, Depends, Header, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer


def get_jwt_token(authorization: str = Header(...)):
    return authorization.split("Bearer ")[1]

images_router = APIRouter()
 
@images_router.post("/images", tags=["Images"], dependencies=[Depends(JWTBearer())])
async def handler_image(request: Request, image: Image = Depends()):
    jwt = get_jwt_token(request.headers.get("authorization"))
    response = ImageService().handler_image(image, token=jwt)
    print(response)               
    return JSONResponse(status_code=200, content=jsonable_encoder(response))
