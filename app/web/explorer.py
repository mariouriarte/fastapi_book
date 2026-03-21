import os
from fastapi import APIRouter, HTTPException
from ..model.explorer import Explorer
from ..errors import Duplicate, Missing

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import explorer as service
else:
    from ..service import explorer as service

router = APIRouter(prefix= "/explorer")

@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}", response_model=Explorer, responses={
    404: {"description": "Explorer not found"},
    400: {"description": "Invalid request or data"}
})
def get_one(name: str) -> Explorer:
    try:
        res = service.get_one(name)
        return Explorer.model_validate(res)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid request parameters")

# all the remaining endpoints do nothing yet:
@router.post("", responses={
    404: {"description": "Duplicate explorer"},
    400: {"description": "Invalid JSON or body"}
})
@router.post("/", responses={
    404: {"description": "Duplicate explorer"},
    400: {"description": "Invalid JSON or body"}
})
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.patch("/", responses={
    404: {"description": "Explorer not found"},
    400: {"description": "Invalid JSON or body"}
})
def modify(name: str, explorer: Explorer) -> Explorer:
    try:
        return service.modify(name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{name}", status_code=204, responses={
    404: {"description": "Explorer not found"},
    400: {"description": "Invalid request"}
})
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

