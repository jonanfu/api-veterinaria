from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import consultation_schema

from app.v1.service import consultation_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/consultation')


@router.post (
    '/',
    tags = ['consultation'],
    status_code = status.HTTP_201_CREATED,
    response_model = consultation_schema.Consultation,
    dependencies = [Depends(get_db)]
)
def create_consultaion (
    consultation: consultation_schema.ConsultationCreate = Body(...),
    current_user: User = Depends(get_current_user)):
    return consultation_service.create_consultation(consultation, current_user)


@router.get (
    '/',
    tags = ['consultation'],
    status_code = status.HTTP_200_OK,
    response_model = List[consultation_schema.Consultation],
    dependencies = [Depends(get_db)]
)
def get_consultations(
    is_done: Optional[bool] = Query(None),
    current_user: User = Depends(get_current_user)
):
    return consultation_service.get_consultation(current_user)


@router.get (
    '/{consultation_id}',
    tags = ['consultation'],
    status_code = status.HTTP_200_OK,
    response_model = consultation_schema.Consultation,
    dependencies = [Depends(get_db)]
)
def get_consultation(
    consultation_id: int = Path (
        ...,
        gt=0
    )
):
    return consultation_service.get_consultation(consultation_id)


@router.patch (
    '/{consultation_id}/update',
    tags = ['consultation'],
    status_code = status.HTTP_200_OK,
    response_model = consultation_schema.Consultation,
    dependencies=[Depends(get_db)]
)
def consultation_update (
    consultation_id: int = Path(
        ...,
        gt=0
    ),
    consultation: consultation_schema.Consultation = Body(...)
):
    return consultation_service.update_consultation(consultation_id,
        date= consultation.date,
        reason_visit= consultation.reason_visit,
        anommesis= consultation.anommesis,
        physical_exam= consultation.physical_exam,
        diagnosis= consultation.diagnosis,
        pathology= consultation.pathology,
        treatment= consultation.treatment,
        recipe= consultation.recipe,
        price= consultation.price,
        send_whatsapp= consultation.send_whatsapp,
        send_email= consultation.send_email,
        send_sms= consultation.send_sms,
        form_payment= consultation.form_payment,
        is_paid= consultation.is_paid,
        #user = user.id,
        vaccine= consultation.vaccine,
        dewormer= consultation.dewormer,
        patient= consultation.patient
    )



@router.delete(
    "/{consultation_id}/",
    tags=["consultation"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_clinic(
    consultation_id: int = Path(
        ...,
        gt=0
    )
):
    consultation_service.delete_consultation(consultation_id)

    return {
        'msg': 'consultation has been deleted sucessfully'
    }
