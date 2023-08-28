import base64
import hashlib
from utils.images_handler import ImageHandler

from schemas.image import Image

# from fastapi import HTTPException
# from jwt_manager.jwt_manager import create_token
# from models.users import User as UserModel
# from schemas.user import User, UserAuth, UserEdit, UserLogin


class ImageService:
    def __init__(self, db) -> None:
        self.db = db

    def handler_image(self, image_data: Image) -> None:
        output_image = ImageHandler(image_data).run()
        print(output_image)
        
                

        return output_image