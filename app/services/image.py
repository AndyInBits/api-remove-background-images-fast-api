import datetime
from redis_config.config import RedisInstance
from utils.images_handler import ImageHandler
from db.session import Session
from models.images import Image as ImageModel
from schemas.image import Image, ImageResponse
from jwt_manager.jwt_manager import validate_token


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