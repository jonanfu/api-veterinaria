from fastapi import HTTPException, status

from app.v1.schema import type_vaccine_schema
from app.v1.model.type_vaccine_model import TypeVaccine as TypeVaccineModel

def create_type_vaccine(type_vaccine: type_vaccine_schema.TypeVaccineCreate):
    db_type_vaccine = TypeVaccineModel(
        name = type_vaccine.name,
        description = type_vaccine.description
    )

    db_type_vaccine.save()

    return type_vaccine_schema.TypeVaccine(
        id = db_type_vaccine.id,
        name = db_type_vaccine.name,
        description = db_type_vaccine.description
    )

def get_type_vaccines():
    type_vaccines = TypeVaccineModel.select().order_by(TypeVaccineModel.id.desc())

    list_type_vaccines = []
    for type_vaccine in type_vaccines:
        list_type_vaccines.append (
            type_vaccine_schema.TypeVaccine(
                id = type_vaccine.id,
                name = type_vaccine.name,
                description = type_vaccine.desciption
            )
        )
    return list_type_vaccines

def get_type_vaccine_by_id(type_vaccine_id: int):
    type_vaccine = TypeVaccineModel.filter(TypeVaccineModel.id == type_vaccine_id).first()

    if not type_vaccine:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Type vaccine not found"
        )

    return type_vaccine_schema.TypeVaccine(
        id = type_vaccine.id,
        name = type_vaccine.name,
        description = type_vaccine.description
    )

def update_type_vaccine(type_vaccine_id: int, 
    name: str = None,
    description: str = None    
    ):

    type_vaccine = TypeVaccineModel.filter(TypeVaccineModel.id == type_vaccine_id).first()

    if not type_vaccine:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Type vaccine not found'
        )
    
    type_vaccine.name = name or type_vaccine.name
    type_vaccine.description = description or type_vaccine.description

    type_vaccine.save()
    return type_vaccine_schema.TypeVaccine(
        id = type_vaccine.id,
        name = type_vaccine.name,
        description = type_vaccine.description

    )
def delete_type_vaccine(type_vaccine_id: int):
    type_vaccine = TypeVaccineModel.filter(TypeVaccineModel.id == type_vaccine_id).first()

    if not type_vaccine:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Type vaccine not found'
        )

    type_vaccine.delete_instance()
