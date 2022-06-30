from fastapi import HTTPException, status

from app.v1.schema import consultation_schema
from app.v1.schema import user_schema
from app.v1.schema import vaccine_schema
from app.v1.schema import dewormer_schema
from app.v1.schema import patient_schema

def create_consultation(
    consultation: consultation_schema.ConsultationCreate,
    user: user_schema.User,
    vaccine: vaccine_schema.Vaccine,
    deworner: dewormer_schema.Deworner,
    patient: patient_schema.Patient
    ):
    pass

def get_consultations():
    pass

def get_consultation(
    consultation_id: int,
    ):
    pass

def get_consultations_by_patient(patient_id: int):
    pass

def update_consultation(
    consultation_id: int,
    user: user_schema.User,
    vaccine: vaccine_schema.Vaccine,
    deworner: dewormer_schema.Deworner,
    patient: patient_schema.Patient,
    ):
    pass

def delete_consultation(consultation_id: int, user: user_schema.User):
    pass

