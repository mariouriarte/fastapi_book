import os
from fastapi import APIRouter, HTTPException
from model.creature import Creature
from errors import Missing, Duplicate

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as service
else:
    from service import creature as service

router = APIRouter(prefix= "/creature")

@router.get("/")
@router.get("")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}", response_model=Creature, responses={
    404: {"description": "Creature not found"},
    400: {"description": "Invalid request or data"}
})
def get_one(name: str) -> Creature:
    try:
        res = service.get_one(name)
        return Creature.model_validate(res)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid request parameters")

@router.post("/", responses={
    404: {"description": "Duplicate creature"},
    400: {"description": "Invalid JSON or body"}
})
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.patch("/", response_model=Creature, responses={
    404: {"description": "Creature not found"},
    400: {"description": "Invalid JSON or body"}
})
def modify(name: str, creature: Creature) -> Creature:
    try:
        return service.modify(name, creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{name}", status_code=204, responses={
    404: {"description": "Creature not found"},
    400: {"description": "Invalid request"}
})
def delete(name: str) -> None:
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

