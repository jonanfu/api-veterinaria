from fastapi import HTTPException, status

from app.v1.schema import type_dewormer_schema
from app.v1.model.type_dewormer_model import TypeDewormer as TypeDewormerModel

def create_type_dewormer(type_dewormer: type_dewormer_schema.TypeDewormerCreate):
    pass

def get_type_dewormers():
    pass

def get_type_dewormer(type_dewormer_id: int):
    pass

def update_type_dewormer(type_dewormer_id: int, type_dewormer: type_dewormer_schema.TypeDewormerUpdate):
    pass

def delete_type_dewormer(type_dewormer_id: int):
    pass
