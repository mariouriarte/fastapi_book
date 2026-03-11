from model.creature import Creature
from errors import Missing, Duplicate

fakes = [
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

def find(name: str) -> Creature | None:
    for e in fakes:
        if e.name == name:
            return e
    return None

def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing creature {name}")

def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"Duplicate creature {name}")

def get_all() -> list[Creature]:
    """Return all creatures"""
    return fakes

def get_one(name: str) -> Creature:
    """Return one creature"""
    check_missing(name)
    return find(name)
    
def create(creature: Creature) -> Creature:
    """Add a creature"""
    check_duplicate(creature.name)
    return creature

def modify(name: str, creature: Creature) -> Creature:
    """Partially modify a creature"""
    check_missing(creature.name)
    return creature

def replace(id, creature: Creature) -> Creature:
    """completely replace an creature"""
    return creature

def delete(name: str) -> None:
    """Delete a creature"""
    check_missing(name)
    return None

