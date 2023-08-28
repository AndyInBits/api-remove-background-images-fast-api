import os
import shutil
from rembg import remove
from fastapi import UploadFile

class ImageHandler:
    file : UploadFile
    upload_dir : str
    output_dir : str
    file_full_path : str
    output_file_full_path : str
    s3_image_url : str

    def __init__(self, file):
        self.file = file
        self.upload_dir = os.path.join(os.getcwd(), "utils/uploads")
        self.output_dir = os.path.join(os.getcwd(), "utils/outputs")
        
    def run (self) -> str:
        self.move_file_tmp_dir()
        self.remove_background_img()
        return self.output_file_full_path
    
    def move_file_tmp_dir(self) -> None:
        self.file_full_path = os.path.join(self.upload_dir, self.file.image.filename)
        with open(self.upload_dir, "wb") as buffer:
            shutil.copyfileobj(self.file.image.file, buffer)


    def remove_background_img(self) -> str:
        self.output_file_full_path = os.path.join(self.output_dir, self.file.image.filename)
        with open(self.file_full_path, "rb") as i:
            with open(self.output_file_full_path, "wb") as o:
                input = i.read()
                output = remove(input)
                o.write(output)

    def resize_image(self) -> None:
        pass

    def save_image_s3(self) -> None:
        return self.s3_image_url
