from fastapi import HTTPException, status

from app.v1.schema import hospitalization_schema
from app.v1.schema import patient_schema
from app.v1.model import hospitalization_model as HospitalizationModel

def create_hospitalization(hospitalization: hospitalization_schema.HospitalizationCreate, patient: patient_schema.Patient):
    pass

def get_hospitalizations():
    pass

def get_hospitalization(hospitalization_id: int):
    pass

def update_hospitalization(hospitalization_id: int, hospitalization: hospitalization_schema.HospitalizationUpdate):
    pass

def delete_hospitalization(hospitalization_id: int):
    pass
