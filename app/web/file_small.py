from fastapi import File
from fastapi import APIRouter
from fastapi import UploadFile
from fastapi.responses import FileResponse

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
