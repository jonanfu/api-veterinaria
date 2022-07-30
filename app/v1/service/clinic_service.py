from fastapi import HTTPException, status

from app.v1.schema import clinic_schema
from app.v1.schema import user_schema
from app.v1.model import clinic_model as ClinicModel

def create_clinic(clinic: clinic_schema.ClinicCreate, user: user_schema.User):
    db_clinic = ClinicModel(
        name = clinic.name,
        addres = clinic.addres,
        city = clinic.city,
        phone = clinic.phone,
        ruc = clinic.ruc,
        user = user.id
    )

    db_clinic.save()

    return clinic_schema.Clinic(
        id = db_clinic.id,
        name = db_clinic.name,
        addres = db_clinic.addres,
        city = db_clinic.city,
        phone = db_clinic.phone,
        ruc = db_clinic.ruc,
        user = db_clinic.user,
        created = db_clinic.created
    )

def get_clinics(user: user_schema.User):
    clinics_by_user = ClinicModel.filter(ClinicModel.user_id, user.id).order_by(ClinicModel.created.desc())

    list_clinics = []
    for clinic in clinics_by_user:
        list_clinics.append(
            clinic_schema.Clinic (
                id = clinic.id,
                name = clinic.name,
                addres = clinic.addres,
                city = clinic.city,
                phone = clinic.phone,
                ruc = clinic.ruc,
                user = clinic.user,
                created = clinic.created
            )
        )
    
    return list_clinics


def get_clinic(clinic_id: int):
    clinic = ClinicModel.filter(ClinicModel.id == clinic_id).first()

    if not clinic:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Clinic not found'
        )

    return clinic_schema.Clinic(
        id = clinic.id,
        name = clinic.name,
        addres = clinic.addres,
        city = clinic.city,
        phone = clinic.phone,
        ruc = clinic.ruc,
        user = clinic.user,
        created = clinic.created
    )

def update_clinic(clinic_id: int,
    name:str = None,
    addres:str = None,
    city:str = None,
    phone:str = None,
    ruc:str = None,
    user:int = None  
):
    clinic = ClinicModel.filter(ClinicModel.id == clinic_id).first()

    if not clinic:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Clinic not found'
        )

    clinic.name = name or clinic.name
    clinic.addres = addres or clinic.addres
    clinic.city = city or clinic.city
    clinic.phone = phone or clinic.phone
    clinic.ruc = ruc or clinic.ruc
    clinic.user  = user or clinic.user

    return clinic_schema.Clinic (
        id = clinic.id,
        name = clinic.name,
        addres = clinic.addres,
        city = clinic.city,
        phone = clinic.phone,
        ruc = clinic.ruc,
        user = clinic.user,
        created = clinic.created
    )
    

def delete_clinic(clinic_id: int):
    clinic = ClinicModel.filter(ClinicModel.id == clinic_id).first()

    if not clinic:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Clinic not found'
        )

    clinic.delete_instance()

