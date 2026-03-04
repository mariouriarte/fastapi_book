from model.creature import Creature
from typing import Optional
# from error import Missing, Duplicate

_creatures = [
    Creature(name="Yeti",
             aka="Abominable Snowman",
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan"),
    Creature(name="Bigfoot",
             description="Yeti's Cousin Eddie",
             country="US",
             area="*",
             aka="Sasquatch"),
    ]

# def find(name: str) -> Creature | None:
#     for e in fakes:
#         if e.name == name:
#             return e
#     return None

# def check_missing(name: str):
#     if not find(name):
#         raise Missing(msg=f"Missing creature {name}")
#
# def check_duplicate(name: str):
#     if find(name):
#         raise Duplicate(msg=f"Duplicate creature {name}")

def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures

def get_one(name: str) -> Optional[Creature]:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

def create(creature: Creature) -> Creature:
    """Add a creature"""
    return creature

def modify(id, creature: Creature) -> Creature:
    """Partially modify a creature"""
    return creature

def replace(id, creature: Creature) -> Creature:
    """completely replace an creature"""
    return creature

def delete(name: str) -> None:
    """Delete a creature"""
    return None

