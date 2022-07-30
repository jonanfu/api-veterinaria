from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import clinic_schema
from app.v1.service import clinic_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/clinic')


@router.post (
    '/',
    tags = ['clinic'],
    status_code = status.HTTP_201_CREATED,
    response_model = clinic_schema.Clinic,
    dependencies = [Depends(get_db)]
)
def create_clinic (
    clinic: clinic_schema.ClinicCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return clinic_service.create_clinic(clinic, current_user)


@router.get (
    '/',
    tags = ['clinic'],
    status_code = status.HTTP_200_OK,
    response_model = List[clinic_schema.Clinic],
    dependencies = [Depends(get_db)]
)
def get_clinic(
    current_user: User = Depends(get_current_user)
):
    return clinic_service.get_clinics(current_user)


@router.get (
    '/{clinic_id}',
    tags = ['clinic'],
    status_code = status.HTTP_200_OK,
    response_model = clinic_schema.Clinic,
    dependencies = [Depends(get_db)]
)
def get_clinic(
    clinic_id: int = Path (
        ...,
        gt=0
    )
):
    return clinic_service.get_clinic(clinic_id)


@router.patch (
    '/{task_id}/update',
    tags = ['clinic'],
    status_code = status.HTTP_200_OK,
    response_model = clinic_schema.Clinic,
    dependencies=[Depends(get_db)]
)
def clinic_update (
    clinic_id: int = Path(
        ...,
        gt=0
    ),
    clinic: clinic_schema.Clinic = Body(...)
    #current_user: User = Depends(get_current_user)
):
    return clinic_service.update_status_task(clinic_id,
        name=clinic.name,
        addres=clinic.addres,
        city=clinic.city,
        phone=clinic.phone,
        ruc=clinic.ruc
        #user=current_user
    )


@router.delete(
    "/{clinic_id}/",
    tags=["clinic"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_clinic(
    clinic_id: int = Path(
        ...,
        gt=0
    )
):
    clinic_service.delete_clinic(clinic_id)

    return {
        'msg': 'clinic has been deleted sucessfully'
    }
