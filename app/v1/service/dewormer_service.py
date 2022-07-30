from datetime import datetime

from fastapi import HTTPException, status

from app.v1.schema import dewormer_schema
from app.v1.model.dewormer_model import Dewormer as DewormerModel

def create_dewormer(dewormer: dewormer_schema.DewormerCreate):
    db_dewormer = DewormerModel (
        date = dewormer.date,
        apply_dewormer = dewormer.apply_dewormer,
        lot = dewormer.lot,
        expiration = dewormer.expiration,
        price = dewormer.price,
        weight = dewormer.weight,
        type_dewormer = dewormer.type_dewormer
    )

    db_dewormer.save()

    return dewormer_schema.Dewormer (
        id = db_dewormer,
        date = db_dewormer.date,
        lot = db_dewormer.lot,
        apply_dewormer = db_dewormer.apply_dewormer,
        expiration = db_dewormer.expiration,
        price = db_dewormer.price,
        weight = db_dewormer.weight,
        type_dewormer = db_dewormer.type_dewormer
    )

def get_dewormers():
    dewormers = DewormerModel.select().order_by(DewormerModel.id.desc())

    list_dewormers = []
    for dewormer in dewormers:
        list_dewormers.append(
            dewormer_schema.Dewormer(
                id = dewormer,
                date = dewormer.date,
                lot = dewormer.lot,
                apply_dewormer = dewormer.apply_dewormer,
                expiration = dewormer.expiration,
                price = dewormer.price,
                weight = dewormer.weight,
                type_dewormer = dewormer.type_dewormer,
                
            )
        )
    
    return list_dewormers

def get_dewormer(dewormer_id: int):
    dewormer = DewormerModel.filter(DewormerModel.id == dewormer_id).first()

    if not dewormer:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Dewormer not found'
        )

    return dewormer_schema.Dewormer (
        id = dewormer,
        date = dewormer.date,
        lot = dewormer.lot,
        apply_dewormer = dewormer.apply_dewormer,
        expiration = dewormer.expiration,
        price = dewormer.price,
        weight = dewormer.weight,
        type_dewormer = dewormer.type_dewormer,
    )        

def update_dewormer(dewormer_id: int, 
    date: datetime = None,
    apply_dewormer:bool = None,
    lot:str = None,
    expiration:datetime = None,
    price: float = None, 
    weight:float = None,
    type_dewormer:int = None,
):
    dewormer = DewormerModel.filter(DewormerModel.id == dewormer_id).first()


    if not dewormer:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Dewormer not found'
        )
    
    dewormer.date = date or dewormer.date
    dewormer.lot = lot or dewormer.lot
    dewormer.apply_dewormer = apply_dewormer or dewormer.apply_dewormer
    dewormer.expiration = expiration or dewormer.expiration
    dewormer.price = price or dewormer.price
    dewormer.weight = weight or dewormer.weight
    dewormer.type_dewormer = type_dewormer or dewormer.type_dewormer
    
    dewormer.save()

    return dewormer_schema.Dewormer (
        id = dewormer,
        date = dewormer.date,
        lot = dewormer.lot,
        apply_dewormer = dewormer.apply_dewormer,
        expiration = dewormer.expiration,
        price = dewormer.price,
        weight = dewormer.weight,
    )
    

def delete_dewormer(dewormer_id: int):
    dewormer = DewormerModel.filter(DewormerModel.id == dewormer_id).first()

    if not dewormer:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Dewormer not found'
        )

    dewormer.delete_instance()
