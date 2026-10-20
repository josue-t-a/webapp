
from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    id: int
    description: str


class ItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    description: str
