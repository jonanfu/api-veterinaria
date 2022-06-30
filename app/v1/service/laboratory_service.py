from fastapi import HTTPException, status

from app.v1.schema import laboratory_schema
from app.v1.model.laboratory_model import Laboratory as LaboratoryModel

def create_laboratory(laboratory: laboratory_schema.LaboratoryCreate):
    pass

def get_laboratories():
    pass

def get_laboratory(laboratory_id: int):
    pass

def update_laboratory(laboratory_id: int, laboratory: laboratory_schema.LaboratoryUpdate):
    pass

def delete_laboratory(laboratory_id: int):
    pass
