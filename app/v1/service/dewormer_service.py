from fastapi import HTTPException, status

from app.v1.schema import dewormer_schema
from app.v1.model.dewormer_model import Deworner as DewornerModel

def create_dewormer(dewormer: dewormer_schema.DewormerCreate):
    pass

def get_dewormers():
    pass

def get_dewormer(dewormer_id: int):
    pass

def update_dewormer(dewormer_id: int, dewormer: dewormer_schema.DewormerUpdate):
    pass

def delete_dewormer(dewormer_id: int):
    pass
