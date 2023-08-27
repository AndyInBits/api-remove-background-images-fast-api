from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, FilePath
from sqlalchemy import Column, Datetime, Float, Integer, String


class ImageFormat(Enum):
    JPEG = 'jpeg'
    PNG = 'png'
    GIF = 'gif'
    BMP = 'bmp'
    TIFF = 'tiff'

class Image(BaseModel):
    id: Optional[int] = None
    format : ImageFormat = Field(default=ImageFormat.PNG)
    width : Optional[int] = Field()
    height : Optional[int] = Field()
    file : FilePath = Field()


    class Config:
        json_schema_extra = {
            "example": {
                "format": ImageFormat.PNG,
                "width": 100,
                "height": 100,
                "file": "image.png"
            }
        }