# encoding: utf-8
import sys

from fastapi import FastAPI

from .routers.img import router as images_router
from .routers.pdf import router as pdfs_router 

app = FastAPI()

@app.get("/")
def ping():
    from qonvert import __version__ as version
    return {"QOnvert server": version}


app.include_router(images_router, prefix="/img")
app.include_router(pdfs_router, prefix="/pdf")
