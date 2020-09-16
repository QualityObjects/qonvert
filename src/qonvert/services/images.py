# encoding: utf-8
'''
Images processing
'''
from PIL import Image, ExifTags
import math, io
from typing import BinaryIO


ORIENTATION_TAG = next( (tag for tag in ExifTags.TAGS.keys() if ExifTags.TAGS[tag]=='Orientation'), None)

async def extract_exif(img_file):
    img : Image = Image.open(img_file)
    exif = {
        ExifTags.TAGS[k]: v
        for k, v in dict(img.getexif()).items()
        if k in ExifTags.TAGS
    }    
    return exif

async def metadata(img_file):
    img : Image = Image.open(img_file)
    return {
        "width": img.width,
        "height": img.height,
        "format": img.format.lower()
    }


def reduce(img_file, max_dim = 1200, output_format = 'JPEG') -> BinaryIO:
    img : Image = reduce_img(img_file, max_dim=max_dim, output_format=output_format)
    exif_data : Image.Exif = img.getexif()

    buff = io.BytesIO()
    img.save(buff, format=output_format, exif=exif_data)
    img_data = buff.getvalue()
    buff.close()
    return io.BytesIO(img_data), len(img_data)

def reduce_img(img_file, max_dim = 1200, output_format = 'JPEG') -> Image:
    img : Image = Image.open(img_file)
    new_size = None
    if (max(img.size) > max_dim):
        coef = max_dim / max(img.size)
        new_size = tuple(map(lambda d: math.floor(d*coef), img.size))
    else:
        new_size = img.size
    exif_data : Image.Exif = img.getexif()
    exif_data[0x011A] = 72 # XResolution
    exif_data[0x011B] = 72 # YResolution

    img = img.resize(new_size, reducing_gap=3.0)
    return img


def fix_orientation(img_file) -> Image:
    '''
    Fix the image orientation based on EXIF image data is exists    
    '''
    if not ORIENTATION_TAG:
        return img_file
    
    img : Image = img_file if Image.isImageType(img_file) else Image.open(img_file) 

    exif = img.getexif()

    if ORIENTATION_TAG in exif:
        if exif[ORIENTATION_TAG] == 3:
            img = img.rotate(180, expand=True)
        elif exif[ORIENTATION_TAG] == 6:
            img = img.rotate(270, expand=True)
        elif exif[ORIENTATION_TAG] == 8:
            img=img.rotate(90, expand=True)

    return img
