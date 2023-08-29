from enum import Enum
from typing import Optional
from fastapi import Form, File, UploadFile
from pydantic import BaseModel, validator
from fastapi import HTTPException

class ImageFormat(Enum):
    JPEG = 'jpeg'
    PNG = 'png'
    GIF = 'gif'
    BMP = 'bmp'
    TIFF = 'tiff'

class Image(BaseModel):
    format_output : ImageFormat = Form(default=ImageFormat.PNG)
    width : Optional[int] = Form(500, gt=0)
    height : Optional[int] = Form(500, gt=0)
    image:  UploadFile = File(...,format=["jpeg","png","gif","bmp","tiff"])

    @validator("image")
    def image_validate(cls, value, values, **kwargs):
        content_types = [
            'image/jpeg',
            'image/png',
            'image/gif',
            'image/bmp',
            'image/tiff'
        ]
        if value.content_type not in content_types:
            raise HTTPException(400, detail="Invalid document type only is allowe : jpeg,png,gif,bmp,tiff")
        return value