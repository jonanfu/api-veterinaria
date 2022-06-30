from fastapi import HTTPException, status

from app.v1.schema import type_vaccine_schema
from app.v1.model.type_vaccine_model import TypeVaccine as TypeVaccineModel

def create_type_vaccine(type_vaccine: type_vaccine_schema.TypeVaccineCreate):
    pass

def get_type_vaccines():
    pass

def get_type_vaccine_by_id(type_vaccine_id: int):
    pass

def update_type_vaccine(type_vaccine_id: int, type_vaccine: type_vaccine_schema.TypeVaccineUpdate):
    pass

def delete_type_vaccine(type_vaccine_id: int):
    pass
