from fastapi import File
from fastapi import APIRouter 

router = APIRouter(prefix= "/file")

@router.post("/small")
async def upload_small_file(small_file: bytes = File()) -> str:
    return f"file size: {len(small_file)}"

# http -f -b POST http://localhost:8000/file/small small_file@1KB.bin
# -f de form ya que se sube un archivo, no se usa json
