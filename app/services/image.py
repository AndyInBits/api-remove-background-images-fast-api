import base64
import datetime
import hashlib
from utils.images_handler import ImageHandler

from models.images import Image as ImageModel
from schemas.image import Image

# from fastapi import HTTPException
from jwt_manager.jwt_manager import validate_token


class ImageService:
    def __init__(self, db) -> None:
        self.db = db

    def handler_image(self, image_data: Image, token: str) -> None:
        user = validate_token(token)
        output_image = ImageHandler(image_data).run()
        new_img = ImageModel(
            user_id=user["id"],
            url_new_file=output_image,
            created_at = datetime.datetime.now()
        )
        self.db.add(new_img)
        self.db.commit()
        self.db.close()

        return new_img