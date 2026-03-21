from pydantic import BaseModel, Field

class Explorer(BaseModel):
    name: str = Field(..., min_length=1, description="Name of the explorer")
    country: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Claude Coleman",
                "country": "US",
                "description": "Expert in mythical creatures"
            }
        }
    }
