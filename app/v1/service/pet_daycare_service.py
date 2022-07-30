from datetime import datetime

from fastapi import HTTPException, status

from app.v1.schema import pet_daycare_schema
from app.v1.model import pet_daycare_model as PetDaycareModel


def create_pet_daycare(pet_daycare: pet_daycare_schema.PetDaycareCreate):
    db_pet_daycare = PetDaycareModel(
        time_eat=pet_daycare.time_eat,
        notes=pet_daycare.notes,
        departure_date=pet_daycare.departure_date,
        moment_payment=pet_daycare.moment_payment,
        price=pet_daycare.price,
        form_payment=pet_daycare.form_payment,
        is_paid=pet_daycare.is_paid,
        patient=pet_daycare.patient
    )

    db_pet_daycare.save()

    return pet_daycare_schema.PayDaycare(
        id=db_pet_daycare.id,
        time_eat=db_pet_daycare.time_eat,
        notes=db_pet_daycare.notes,
        admission_date=db_pet_daycare.admission_date,
        departure_date=db_pet_daycare.departure_date,
        moment_payment=db_pet_daycare.moment_payment,
        price=db_pet_daycare.price,
        form_payment=db_pet_daycare.form_payment,
        is_paid=db_pet_daycare.is_paid,
        patient=db_pet_daycare.patient
    )


def get_pet_daycares():
    pet_daycares = PetDaycareModel.Select().order_by(PetDaycareModel.id.desc())

    list_pet_daycares = []
    for pet_daycare in pet_daycare:
        list_pet_daycares.append(
            pet_daycare_schema.PayDaycare(
                id=pet_daycare.id,
                time_eat=pet_daycare.time_eat,
                notes=pet_daycare.notes,
                admission_date=pet_daycare.admission_date,
                departure_date=pet_daycare.departure_date,
                moment_payment=pet_daycare.moment_payment,
                price=pet_daycare.price,
                form_payment=pet_daycare.form_payment,
                is_paid=pet_daycare.is_paid,
                patient=pet_daycare.patient
            )
        )

    return pet_daycare_schema.PayDaycare(
        id=pet_daycare.id,
        time_eat=pet_daycare.time_eat,
        notes=pet_daycare.notes,
        admission_date=pet_daycare.admission_date,
        departure_date=pet_daycare.departure_date,
        moment_payment=pet_daycare.moment_payment,
        price=pet_daycare.price,
        form_payment=pet_daycare.form_payment,
        is_paid=pet_daycare.is_paid,
        patient=pet_daycare.patient
    )


def get_pet_daycare(pet_daycare_id: int):
    pet_daycare = PetDaycareModel.filter(
        PetDaycareModel.id == pet_daycare_id).first()

    if not pet_daycare:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Pet daycare not found'
        )

    return pet_daycare_schema.PayDaycare(
        id=pet_daycare.id,
        time_eat=pet_daycare.time_eat,
        notes=pet_daycare.notes,
        admission_date=pet_daycare.admission_date,
        departure_date=pet_daycare.departure_date,
        moment_payment=pet_daycare.moment_payment,
        price=pet_daycare.price,
        form_payment=pet_daycare.form_payment,
        is_paid=pet_daycare.is_paid,
        patient=pet_daycare.patient
    )


def update_pet_daycare(pet_daycare_id: int,
                       time_eat: datetime = None,
                       notes: str = None,
                       departure_date: datetime = None,
                       moment_payment: str = None,
                       price: float = None,
                       form_payment: str = None,
                       is_paid: bool = None,
                       patient: int = None
                       ):
    pet_daycare = PetDaycareModel.filter(
        PetDaycareModel.id == pet_daycare_id).first()

    if not pet_daycare:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Pet daycare not found'
        )

    pet_daycare.time_eat = time_eat or pet_daycare.time_eat
    pet_daycare.notes = notes or pet_daycare.notes
    pet_daycare.departure_date = departure_date or pet_daycare.departure
    pet_daycare.moment_payment = moment_payment or pet_daycare.moment_payment
    pet_daycare.price = price or pet_daycare.price
    pet_daycare.form_payment = form_payment or pet_daycare.form_payment
    pet_daycare.is_paid = is_paid or pet_daycare.is_paid
    pet_daycare.patient = patient or pet_daycare.patient

    pet_daycare.save()

    return pet_daycare_schema.PayDaycare(
        id=pet_daycare.id,
        time_eat=pet_daycare.time_eat,
        notes=pet_daycare.notes,
        admission_date=pet_daycare.admission_date,
        departure_date=pet_daycare.departure_date,
        moment_payment=pet_daycare.moment_payment,
        price=pet_daycare.price,
        form_payment=pet_daycare.form_payment,
        is_paid=pet_daycare.is_paid,
        patient=pet_daycare.patient
    )


def delete_pet_daycare(pet_daycare_id: int):
    pet_daycare = PetDaycareModel.filter(
        PetDaycareModel.id == pet_daycare_id).first()

    if not pet_daycare:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Pet daycare not found'
        )

    pet_daycare.delelte_isntance()
