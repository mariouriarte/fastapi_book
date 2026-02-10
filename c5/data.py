from model.model import Creature

_creatures: list[Creature] = [
    Creature(name="yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman"
    ),
    Creature(name="sasquatch",
        country="US",
        area="*",
        description="Yeti's Cousin Eddie",
        aka="Bigfoot"),
    Creature(name="sasquatch 2",
        country="US",
        area="*",
        description="Yeti's Cousin Eddie 2",
        aka="Bigfoot 2")
]

def get_creatures() -> list[Creature]:
    return _creatures
