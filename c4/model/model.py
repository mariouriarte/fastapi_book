from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str

thing = Creature(
    country="CN",
    name="yeti",
    area="Himalayas",
    description="Hirsute himalaya",
    aka="Abominable Snowman"
)
print("name is", thing.name)
