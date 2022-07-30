from datetime import datetime
from fastapi import HTTPException, status

from app.v1.schema import esthetic_schema
from app.v1.schema import patient_schema
from app.v1.model.esthetic_model import Esthetic as EstheticModel


def create_esthetic(esthetic: esthetic_schema.EstheticCreate, patient: patient_schema.Patient):
    db_esthetic = EstheticModel(
        date=esthetic.date,
        hour=esthetic.hour,
        activate_notification=esthetic.activate_notification,
        price=esthetic.price,
        form_payment=esthetic.form_payment,
        is_paid=esthetic.is_paid,
        patient=esthetic.patient
    )

    db_esthetic.save()

    return esthetic_schema.Esthetic(
        id=db_esthetic.id,
        date=db_esthetic.date,
        hour=db_esthetic.hour,
        activate_notification=db_esthetic.activate_notification,
        price=db_esthetic.price,
        form_payment=db_esthetic.form_payment,
        is_paid=db_esthetic.is_paid,
        patient=db_esthetic.patient
    )


def get_esthetics():
    esthectics = EstheticModel.select().order_by(EstheticModel.id.desc())

    list_esthetics = []
    for esthetic in esthectics:
        list_esthetics.append(
            esthetic_schema.Esthetic(
                id=esthetic.id,
                date=esthetic.date,
                hour=esthetic.hour,
                activate_notification=esthetic.activate_notification,
                price=esthetic.price,
                form_payment=esthetic.form_payment,
                is_paid=esthetic.is_paid,
                patient=esthetic.patient
            )
        )


def get_esthetic(esthetic_id: int):
    esthetic = EstheticModel.filter(EstheticModel.id == esthetic_id).first()

    if not esthetic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Esthetic not found'
        )

    return esthetic_schema.Esthetic(
        id=esthetic.id,
        date=esthetic.date,
        hour=esthetic.hour,
        activate_notification=esthetic.activate_notification,
        price=esthetic.price,
        form_payment=esthetic.form_payment,
        is_paid=esthetic.is_paid,
        patient=esthetic.patient
    )


def update_esthetic(esthetic_id: int,
                    date: datetime = None,
                    hour: datetime = None,
                    activate_notification: bool = None,
                    price: float = None,
                    form_payment: str = None,
                    is_paid: bool = None,
                    patient: int = None
                    ):
    esthetic = EstheticModel.filter(EstheticModel.id == esthetic_id).first()

    if not esthetic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Esthetic not found'
        )

    esthetic.date = date or esthetic.date
    esthetic.hour = hour or esthetic.hour
    esthetic.activate_notification = activate_notification or esthetic.activate_notification
    esthetic.price = price or esthetic.price
    esthetic.form_payment = form_payment or esthetic.form_payment
    esthetic.is_paid = is_paid or esthetic.is_paid
    esthetic.patient = patient or esthetic.patient

    esthetic.save()

    return esthetic_schema.Esthetic(
        id=esthetic.id,
        date=esthetic.date,
        hour=esthetic.hour,
        activate_notification=esthetic.activate_notification,
        price=esthetic.price,
        form_payment=esthetic.form_payment,
        is_paid=esthetic.is_paid,
        patient=esthetic.patient
    )


def delete_esthetic(esthetic_id: int):
    esthetic = EstheticModel.filter(EstheticModel.id == esthetic_id).first()

    if not esthetic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Esthetic not found'
        )

    esthetic.delete_instance()
