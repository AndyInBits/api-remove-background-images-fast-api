import os
import shutil
from rembg import remove


class ImageHandler:
    @staticmethod
    def load_image_input_dir(image_data) -> tuple[str, str]:
        upload_dir = os.path.join(os.getcwd(), "utils/uploads")
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        input_dir = os.path.join(upload_dir, image_data.image.filename)
        with open(input_dir, "wb") as buffer:
            shutil.copyfileobj(image_data.image.file, buffer)
        output_dir = os.path.join(os.getcwd(), "outputs")
        return input_dir, output_dir

    @staticmethod
    def remove_background_img(image_data, input_dir, output_dir) -> str:
        output_dir = output_dir + "/" + image_data.image.filename
        with open(input_dir, "rb") as i:
            with open(output_dir, "wb") as o:
                input = i.read()
                output = remove(input)
                o.write(output)
        return output_dir
