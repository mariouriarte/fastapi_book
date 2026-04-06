from os import name
from typing import Generator
from fastapi import File
from fastapi import APIRouter
from fastapi import UploadFile
from fastapi.responses import FileResponse, StreamingResponse


router = APIRouter(prefix= "/file")

@router.post("/small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"

# http -f -b POST http://localhost:8000/file/small small_file@1KB.bin
# -f de form ya que se sube un archivo, no se usa json

# para crear un archivo
# dd if=/dev/urandom of=1KB.bin bs=1024 count=1

@router.get("/small/{name}")
async def download_small_file(name):
    return FileResponse(name)

@router.post("/big")
async def upload_big_file(big_file: UploadFile) -> str:
    return f"file size: {big_file.size}, name: {big_file.filename}"

def gen_file(path: str) -> Generator:
    with open(file=path, mode="rb") as file:
        yield file.read()

@router.get("/big/{name}")
async def download_big_file(name:str):
    gen_expr = gen_file(path=name)
    response = StreamingResponse(
        content=gen_expr,
        status_code=200,
    )
    return response


