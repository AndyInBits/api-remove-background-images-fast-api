import datetime

from db.session import Session
from fastapi import HTTPException
from jwt_manager.jwt_manager import validate_token
from models.images import Image as ImageModel
from redis_config.config import RedisInstance
from schemas.image import Image, ImageResponse
from utils.images_handler import ImageHandler


class ImageService:
    def __init__(self) -> None:
        self.db = Session()


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
        response = ImageResponse(
            id=new_img.id,
            url_new_file=new_img.url_new_file,
            created_at=new_img.created_at,
            user_id=new_img.user_id
        )
        self.db.close()
        return response
    
    def get_all_images_from_user(self, jwt):
        user = validate_token(jwt)
        images = self.db.query(ImageModel).filter(ImageModel.user_id == user["id"]).all()
        return images
    
    def delete_image_from_user(self, jwt, img_id):
        user = validate_token(jwt)
        image = self.db.query(ImageModel).filter(ImageModel.id == img_id, ImageModel.user_id == user["id"]).first()
        if not image:
            raise HTTPException(status_code=404, detail="Image not found")
        self.db.delete(image)
        self.db.commit()
        self.db.close()
    

