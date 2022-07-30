from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import patient_schema
from app.v1.service import patient_service
from app.v1.schema import species_schema
from app.v1.schema import breed_shema
from app.v1.schema import client_schema
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/patient')


@router.post (
    '/',
    tags = ['patient'],
    status_code = status.HTTP_201_CREATED,
    response_model = patient_schema.Patient,
    dependencies = [Depends(get_db)]
)
def create_patient (
    patient: patient_schema.PatientCreate = Body(...),
):
    return patient_service.create_patient(patient)


@router.get (
    '/',
    tags = ['patient'],
    status_code = status.HTTP_200_OK,
    response_model = List[patient_schema.Patient],
    dependencies = [Depends(get_db)]
)
def get_patient():
    return patient_service.get_patients()


@router.get (
    '/{patient_id}',
    tags = ['patient'],
    status_code = status.HTTP_200_OK,
    response_model = patient_schema.Patient,
    dependencies = [Depends(get_db)]
)
def get_patient(
    patient_id: int = Path (
        ...,
        gt=0
    )
):
    return patient_service.get_task(patient_id)


@router.patch (
    '/{patient_id}/update',
    tags = ['patient'],
    status_code = status.HTTP_200_OK,
    response_model = patient_schema.Patient,
    dependencies=[Depends(get_db)]
)
def patient_update (
    patient_id: int = Path(
        ...,
        gt=0
    ),
    patient: patient_schema.Patient = Body(...)
):
    return patient_service.update_patient(patient_id, 
        name = patient.name,
        birthday = patient.birthday,
        years = patient.years,
        months = patient.months,
        gender = patient.gender,
        fur = patient.fur,
        food_consumer = patient.food_consumer,
        is_heat = patient.is_heat,
        is_pedigree = patient.is_pedigree,
        is_reproductive = patient.is_reproductive,
        is_castrated = patient.is_castrated,
        pathologies = patient.pathologies,
        photo = patient.photo,
        chip = patient.chip,
        aggresive = patient.aggresive,
        is_dead = patient.is_dead,
        specie = patient.specie,
        breed = patient.breed,
        client = patient.client
    )


@router.delete(
    "/{patient_id}/",
    tags=["patient"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_patient(
    patient_id: int = Path(
        ...,
        gt=0
    )
):
    patient_service.delete_patient(patient_id)

    return {
        'msg': 'Patient has been deleted sucessfully'
    }
