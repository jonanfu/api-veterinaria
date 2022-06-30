from fastapi import HTTPException, status

from app.v1.schema import esthetic_schema
from app.v1.schema import patient_schema
from app.v1.model.esthetic_model import Esthetic as EstheticModel

def create_esthetic(esthetic: esthetic_schema.EstheticCreate, patient: patient_schema.Patient):
    pass

def get_esthetics():
    pass

def get_esthetic(esthetic_id: int):
    pass

def update_esthetic(esthetic_id: int, esthetic: esthetic_schema.EstheticUpdate):
    pass

def delete_esthetic(esthetic_id: int):
    pass
