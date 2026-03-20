from pydantic import BaseModel, Field

class Creature(BaseModel):
    name: str = Field(..., min_length=1, description="Unique name of the creature")
    country: str = Field(..., min_length=1)
    area: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    aka: str = Field(..., min_length=1)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Dragon",
                "country": "IS",
                "area": "Cloudy Mountains",
                "description": "Large fire-breathing reptile",
                "aka": "Firedrake"
            }
        }
    }
