import io
import os
import shutil
import uuid
from rembg import remove
from fastapi import UploadFile
import boto3
from core.config import settings
from PIL import Image

class ImageHandler:
    file: UploadFile
    upload_dir: str
    output_dir: str
    height: int
    width: int
    output_format : str
    file_full_path: str
    output_file_full_path: str
    s3_image_url: str

    def __init__(self, file):
        self.file = file.image
        self.height = file.height
        self.width = file.width
        self.output_format = file.format_output.value
        self.upload_dir = os.path.join(os.getcwd(), "utils/statics/uploads")
        self.output_dir = os.path.join(os.getcwd(), "utils/statics/outputs")

    def run(self) -> str:
        self.move_file_tmp_dir()
        self.remove_background_img()
        self.resize_image()
        self.delete_file_tmp_dir()

        return self.s3_image_url

    def move_file_tmp_dir(self) -> None:
        self.file_full_path = os.path.join(self.upload_dir, self.file.filename)
        with open(self.file_full_path, "wb") as buffer:
            shutil.copyfileobj(self.file.file, buffer)

    def remove_background_img(self) -> str:
        self.output_file_full_path = os.path.join(self.output_dir, self.file.filename)
        with open(self.file_full_path, "rb") as i:
            with open(self.output_file_full_path, "wb") as o:
                input = i.read()
                output = remove(input)
                o.write(output)

    def resize_image(self) -> None:
        with open(self.output_file_full_path, "rb") as o:
                input = o.read()
                image = Image.open(io.BytesIO(input))
                image = image.resize((self.width, self.height), Image.Resampling.LANCZOS)
                temp = io.BytesIO()
                image = image.convert('RGB')
                image.save(temp, format=self.output_format, quality=60)
                temp.seek(0)
                self._save_image_s3(temp.read())

    def _save_image_s3(self, image) -> None:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.S3_ACCESS_KEY,
            aws_secret_access_key=settings.S3_SECRET_KEY,
        )
        file_name = str(uuid.uuid4()) + "-" + self.file.filename
        self.s3_image_url = f"{settings.S3_HOST}{file_name}"
        
        s3.upload_fileobj(
                Fileobj=io.BytesIO(image),
                Bucket=settings.S3_BUCKET,
                Key="downloads/" + file_name,
                ExtraArgs={
                    "ContentType": 'image/' + self.output_format
                }
            )
        
    def delete_file_tmp_dir(self) -> None:
        os.remove(self.file_full_path)
        os.remove(self.output_file_full_path)