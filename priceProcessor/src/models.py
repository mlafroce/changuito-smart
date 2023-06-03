import uuid
from pydantic import BaseModel, Field


class Location(BaseModel):
    address: str
    lat: str
    long: str
    city: str


class Branch(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    branch_id: str = Field(...)
    name: str
    location: Location
    trade_name: str

    class Config:
        allow_population_by_field_name = True
        # schema_extra = {
        #     "example": {
        #         "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
        #         "title": "Don Quixote",
        #         "author": "Miguel de Cervantes",
        #         "synopsis": "..."
        #     }
        # }
