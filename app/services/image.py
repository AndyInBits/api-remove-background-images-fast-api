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
        input_image , output_image = ImageHandler.load_image_input_dir(image_data)
        output_image = ImageHandler.remove_background_img(image_data,input_image, output_image)

        
                

        return output_image