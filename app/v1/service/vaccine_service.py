from datetime import datetime

from fastapi import HTTPException, status

from app.v1.schema import vaccine_schema
from app.v1.schema import type_vaccine_schema
from app.v1.model.vaccine_model import Vaccine as VaccineModel

def create_vaccine(vaccine: vaccine_schema.VaccineCreate):
    db_vaccine = VaccineModel (
        date = vaccine.date,
        lot = vaccine.lot,
        apply_vaccine = vaccine.apply_vaccine,
        expiration = vaccine.expiration,
        price = vaccine.price,
        weight = vaccine.weight,
        previous_vaccinations = vaccine.previous_vaccinations,
        type_vaccine = vaccine.type_vaccine
    )

    db_vaccine.save()

    return vaccine_schema.Vaccine (
        id = db_vaccine,
        date = db_vaccine.date,
        lot = db_vaccine.lot,
        apply_vaccine = db_vaccine.apply_vaccine,
        expiration = db_vaccine.expiration,
        price = db_vaccine.price,
        weight = db_vaccine.weight,
        previous_vaccinations = db_vaccine.previous_vaccinations,
        type_vaccine = db_vaccine.type_vaccine,
        created_at = db_vaccine.created_at
    )

def get_vaccines():
    vaccines = VaccineModel.select().order_by(VaccineModel.id.desc())

    list_vaccines = []
    for vaccine in vaccines:
        list_vaccines.append(
            vaccine_schema.Vaccine(
                id = vaccine,
                date = vaccine.date,
                lot = vaccine.lot,
                apply_vaccine = vaccine.apply_vaccine,
                expiration = vaccine.expiration,
                price = vaccine.price,
                weight = vaccine.weight,
                previous_vaccinations = vaccine.previous_vaccinations,
                type_vaccine = vaccine.type_vaccine,
                created_at = vaccine.created_at
            )
        )
    
    return list_vaccines

def get_vaccine_by_id(vaccine_id: int):
    vaccine = VaccineModel.filter(VaccineModel.id == vaccine_id).first()

    if not vaccine:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Vaccine not found'
        )

    return vaccine_schema.Vaccine (
        id = vaccine,
        date = vaccine.date,
        lot = vaccine.lot,
        apply_vaccine = vaccine.apply_vaccine,
        expiration = vaccine.expiration,
        price = vaccine.price,
        weight = vaccine.weight,
        previous_vaccinations = vaccine.previous_vaccinations,
        type_vaccine = vaccine.type_vaccine,
        created_at = vaccine.created_at
    )        

def update_vaccine(vaccine_id: int, 
    date:datetime = None,
    lot:str = None,
    apply_vaccine:bool = None,
    expiration:datetime = None,
    price: float = None, 
    weight:float = None,
    previous_vaccinations:bool = None,
    type_vaccine:int = None,
):
    vaccine = VaccineModel.filter(VaccineModel.id == vaccine_id).first()

    if not vaccine:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Vaccine not found'
        )
    
    vaccine.date = date or vaccine.date
    vaccine.lot = lot or vaccine.lot
    vaccine.apply_vaccine = apply_vaccine or vaccine.apply_vaccine
    vaccine.expiration = expiration or vaccine.expiration
    vaccine.price = price or vaccine.price
    vaccine.weight = weight or vaccine.weight
    vaccine.previous_vaccinations = previous_vaccinations or vaccine.previous_vaccinations
    vaccine.type_vaccine = type_vaccine or vaccine.type_vaccine
    
    vaccine.save()

    return vaccine_schema.Vaccine (
        id = vaccine,
        date = vaccine.date,
        lot = vaccine.lot,
        apply_vaccine = vaccine.apply_vaccine,
        expiration = vaccine.expiration,
        price = vaccine.price,
        weight = vaccine.weight,
        previous_vaccinations = vaccine.previous_vaccinations,
        type_vaccine = vaccine.type,
        created_at = vaccine.created_at
    )

def delete_vaccine(vaccine_id: int):
    vaccine = VaccineModel.filter(VaccineModel.id == vaccine_id).first()

    if not vaccine:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Vaccine not found'
        )

    vaccine.delete_instance()
