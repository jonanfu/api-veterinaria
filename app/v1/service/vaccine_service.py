from fastapi import HTTPException, status

from app.v1.schema import vaccine_schema
from app.v1.schema import type_vaccine_schema
from app.v1.model.vaccine_model import Vaccine as VaccineModel

def create_vaccine(vaccine: vaccine_schema.VaccineCreate):
    pass

def get_vaccines():
    pass

def get_vaccine_by_id(vaccine_id: int):
    pass

def update_vaccine(vaccine_id: int, vaccine: vaccine_schema.VaccineUpdate):
    pass

def delete_vaccine(vaccine_id: int):
    pass
