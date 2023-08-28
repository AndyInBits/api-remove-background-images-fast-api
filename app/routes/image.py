from services.image import ImageService
from schemas.image import Image
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db.session import Session

images_router = APIRouter()

@images_router.post("/images", tags=["Images"])
def handler_image(image: Image = Depends()):
    db = Session()
    response = ImageService(db).handler_image(image)
    return JSONResponse(status_code=200, content=response)
