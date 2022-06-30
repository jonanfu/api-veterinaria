from fastapi import HTTPException, status

from app.v1.schema import pet_daycare_schema
from app.v1.schema import patient_schema
from app.v1.model import pet_daycare_model as PetDaycareModel

def create_pet_daycare(pet_daycare: pet_daycare_schema.PetDaycareCreate, patient: patient_schema.Patient):
    pass

def get_pet_daycares():
    pass

def get_pet_daycare(pet_daycare_id: int):
    pass

def update_pet_daycare(pet_daycare_id: int, pet_daycare: pet_daycare_schema.PetDaycareUpdate):
    pass

def delete_pet_daycare(pet_daycare_id: int):
    pass
