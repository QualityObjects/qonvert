# encoding: utf-8

import sys

from fastapi import APIRouter, File, Form, UploadFile
from starlette.responses import StreamingResponse
from ..services import images 
router = APIRouter()


@router.get("/")
async def index():
    return 'Images API'


@router.post("/exif")
async def read_exif(hola: str = Form(...), f: UploadFile = File(...)):
    result = {
        "filename": f.filename,
        "content-type": f.content_type,
        "exif": await images.extract_exif(f.file),
        "metadata": await images.metadata(f.file)
    }
    return result


@router.post("/reduce")
def convert(f: UploadFile = File(...), output_format: str = 'JPEG', max_dim: int = 1200):
    img_buffer, img_size = images.reduce(f.file, max_dim, output_format)
    return StreamingResponse(img_buffer, media_type=f'image/{output_format.lower()}',
                    headers= {
                        'Content.Length': str(img_size)
                    })






