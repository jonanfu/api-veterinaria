from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import patient_schema
from app.v1.service import patient_service
from app.v1.schema import species_schema
from app.v1.schema import breed_shema
from app.v1.schema import client_shema
from app.v1.utils import get_db
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
    current_user: User = Depends(get_current_user)):
    return patient_service.create_patient(patient, current_user)


@router.get (
    '/',
    tags = ['patient'],
    status_code = status.HTTP_200_OK,
    response_model = List[patient_schema.Patient],
    dependencies = [Depends(get_db)]
)
def get_patient(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return patient_service.get_patients(current_user, is_done)


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
    ),
    current_user: User = Depends(get_current_user)
):
    return patient_service.get_task(patient_id, current_user)


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
    current_user: User = Depends(get_current_user)
):
    return patient_service.update_status_task(patient_id, current_user)


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
    ),
    current_user: User = Depends(get_current_user)
):
    patient_service.delete_patient(patient_id, current_user)

    return {
        'msg': 'patient has been deleted sucessfully'
    }
