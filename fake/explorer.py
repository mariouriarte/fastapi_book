from typing import Optional
from model.explorer import Explorer
# from error import Missing, Duplicate

_explorers = [
    Explorer(name="Claude Hande",
             country="FR",
             description="Scarce during full moons"),
    Explorer(name="Noah Weiser",
             country="DE",
             description="Myopic machete man"),
    ]

# def find(name: str) -> Explorer | None:
#     for e in fakes:
#         if e.name == name:
#             return e
#     return None

# def check_missing(name: str):
#     if not find(name):
#         raise Missing(msg=f"Missing explorer {name}")
#
# def check_duplicate(name: str):
#     if find(name):
#         raise Duplicate(msg=f"Duplicate explorer {name}")

def get_all() -> list[Explorer]:
    """Return all explorers"""
    return _explorers

def get_one(name: str) -> Optional[Explorer]:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    """Add a explorer"""
    return explorer

def modify(id, explorer: Explorer) -> Explorer:
    """Partially modify a explorer"""
    return explorer

def replace(id, explorer: Explorer) -> Explorer:
    """completely replace an explorer"""
    return explorer

def delete(name: str) -> None:
    """Delete a explorer"""
    return None
