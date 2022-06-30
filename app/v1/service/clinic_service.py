from fastapi import HTTPException, status

from app.v1.schema import clinic_shema
from app.v1.schema import user_schema
from app.v1.model import clinic_model as ClinicModel

def create_clinic(clinic: clinic_shema.ClinicCreate, user: user_schema.User):
    pass

def get_clinics(clinic_id: int):
    pass

def get_clinic(clinic_id: int):
    pass

def update_clinic(clinic_id: int, clinic: clinic_shema.ClinicUpdate):
    pass

def delete_clinic(clinic_id: int):
    pass

