from fastapi import HTTPException, status

from app.v1.schema import laboratory_schema
from app.v1.model.laboratory_model import Laboratory as LaboratoryModel

def create_laboratory(laboratory: laboratory_schema.LaboratoryCreate):
    db_laboratory = LaboratoryModel(
        name = laboratory.name,
        description = laboratory.description
    )

    db_laboratory.save()

    return laboratory_schema.Laboratory(
        id = db_laboratory.id,
        name = db_laboratory.name,
        description = db_laboratory.description
    )


def get_laboratories():
    laboratories = LaboratoryModel.select().order_by(LaboratoryModel.id.desc())

    list_laboratories = []
    for laboratory in laboratories:
        list_laboratories.append(
            laboratory_schema.Laboratory(
                id = laboratory.id,
                name = laboratory.name,
                description = laboratory.description
            )
        )
    
    return list_laboratories

def get_laboratory(laboratory_id: int):
    laboratory = LaboratoryModel.filter(LaboratoryModel.id == laboratory_id).first()

    if not laboratory:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Laboratory not found"
        )
    
    return laboratory_schema.Laboratory(
        id = laboratory.id,
        name = laboratory.name,
        description = laboratory.description
    )
    

def update_laboratory(laboratory_id: int,
    name = None,
    description = None):
    
    laboratory = LaboratoryModel.filter(LaboratoryModel.id == laboratory_id).first()

    if not laboratory:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Laboratory not found"
        )

    laboratory.name = name
    laboratory.description = description

    laboratory.save()

    return laboratory_schema.Laboratory(
        id = laboratory.id,
        name = laboratory.name,
        description = laboratory.description
    )
    

def delete_laboratory(laboratory_id: int):
    laboratory = LaboratoryModel.filter(LaboratoryModel.id == laboratory_id).first()

    if not laboratory:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Laboratory not found"
        )

    laboratory.delete_instance()

    
