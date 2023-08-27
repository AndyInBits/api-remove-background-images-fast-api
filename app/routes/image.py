from schemas.image import Image
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

images_router = APIRouter()

@images_router.post("/images", tags=["Images"])
def handler_image(image: Image = Depends()):
    print(image)
    return JSONResponse(status_code=200, content="OK")
