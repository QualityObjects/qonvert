# encoding: utf-8
'''
PDFs processing

'''
import sys

from typing import BinaryIO, List 
from PIL import Image, ExifTags
import math, io
from .images import reduce_img, fix_orientation

def pdf_from_images(img_files : List[BinaryIO], max_dim : int = 1200) -> BinaryIO:
    opt_images = []
    for img_file in img_files:
        img : Image = reduce_img(img_file, max_dim=1200)        
        opt_images.append(fix_orientation(img))
        #opt_images.append(img)

    buff = io.BytesIO() 
    opt_images[0].save(buff, format='PDF', resolution=72.0, save_all=True, append_images=opt_images[1:])
    pdf_data = buff.getvalue()
    buff.close() 
    return io.BytesIO(pdf_data), len(pdf_data)