__author__ = 'Santhosh'
from PIL import Image
import StringIO

def create_thumbnail(size,image_buffer,image_name, file_path ):
    img = Image.open(StringIO.StringIO(image_buffer))
    img.thumbnail(size, Image.ANTIALIAS)
    image_file = file_path+image_name
    img.save(image_file, "JPEG")
    return image_file