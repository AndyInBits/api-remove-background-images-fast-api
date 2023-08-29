from services.image import ImageService
from schemas.image import Image
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db.session import Session
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from fastapi.encoders import jsonable_encoder


images_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@images_router.post("/images", tags=["Images"])
async def handler_image(token: Annotated[str, Depends(oauth2_scheme)], image: Image = Depends()):
    db = Session()
    response = ImageService(db).handler_image(image, await token)
    print(response)               
    return JSONResponse(status_code=200, content=jsonable_encoder(response))
