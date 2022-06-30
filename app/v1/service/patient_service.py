from fastapi import HTTPException, status

from app.v1.schema import patient_schema
from app.v1.schema import species_schema
from app.v1.schema import breed_schema
from app.v1.schema import client_shema
from app.v1.model import patient_model as PatientModel

def create_patient(
    patient: patient_schema.PatientCreate,
    species: species_schema.Species,
    breed: breed_schema.Breed,
    client: client_shema.Client):
    pass

def get_patients():
    pass

def get_patient(patient_id: int):
    pass

def update_patient(patient_id: int, patient: patient_schema.PatientUpdate):
    pass

def delete_patient(patient_id: int):
    pass
