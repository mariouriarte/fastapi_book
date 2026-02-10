from pydantic import BaseModel, constr, Field

class Creature(BaseModel):
    name: constr(min_length=2)
    country: str = Field(..., min_length=2)
    area: str
    description: str
    aka: str

thing = Creature(
    country="CN",
    name="yi",
    area="Himalayas",
    description="Hirsute himalaya",
    aka="Abominable Snowman"
)
print("name is", thing.name)
