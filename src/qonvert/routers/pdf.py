# encoding: utf-8

import sys

from fastapi import APIRouter, File, Form, UploadFile
from starlette.responses import StreamingResponse
from ..services import pdfs 
from typing import List

router = APIRouter()
 

@router.get("/")
async def index():
    return 'PDFs API'

@router.post("/from_images")
def convert(files: List[UploadFile] = File(...), max_dim: int = 1200):
    pdf_buffer, pdf_size = pdfs.pdf_from_images((f.file for f in files), max_dim)
    return StreamingResponse(pdf_buffer, 
                    media_type='application/pdf', 
                    headers= { 'Content.Length': str(pdf_size) })






