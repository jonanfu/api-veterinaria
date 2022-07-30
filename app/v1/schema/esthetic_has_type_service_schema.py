#Python
from datetime import datetime

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class EstheticHasTypeServiceCreate(BaseModel):
    esthetic:int = Field(...)
    type_service:int = Field(...)

class EstheticHasTypeService(EstheticHasTypeServiceCreate):
    id: int = Field(...)
    