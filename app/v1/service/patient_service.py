from fastapi import HTTPException, status

from app.v1.schema import patient_schema
from app.v1.model import patient_model as PatientModel

def create_patient(patient: patient_schema.PatientCreate):
    db_patient = PatientModel (
        name = patient.name,
        birthday = patient.birthday,
        years = patient.years,
        months = patient.months,
        gender = patient.gender,
        fur = patient.fur,
        food_consumer = patient.food_consumer,
        is_heat = patient.is_heat,
        is_pedigree = patient.is_pedigree,
        is_reproductive = patient.is_reproductive,
        is_castrated = patient.is_castrated,
        pathologies = patient.pathologies,
        photo = patient.photo,
        chip = patient.chip,
        aggresive = patient.aggresive,
        specie = patient.specie,
        breed = patient.breed,
        client = patient.client,
    )

    db_patient.save()

    return patient_schema.Patient(
        id = db_patient.id,
        name = db_patient.name,
        birthday = db_patient.birthday,
        years = db_patient.years,
        months = db_patient.months,
        gender = db_patient.gender,
        fur = db_patient.fur,
        food_consumer = db_patient.food_consumer,
        is_heat = db_patient.is_heat,
        is_pedigree = db_patient.is_pedigree,
        is_reproductive = db_patient.is_reproductive,
        is_castrated = db_patient.is_castrated,
        pathologies = db_patient.pathologies,
        photo = db_patient.photo,
        chip = db_patient.chip,
        aggresive = db_patient.aggresive,
        is_dead = db_patient.is_dead,
        specie = db_patient.specie,
        breed = db_patient.breed,
        client = db_patient.client,
    )

def get_patients():
    patients = PatientModel.select().order_by(PatientModel.id.desc())

    list_patients = []

    for patient in patients:
        list_patients.append(
            patient_schema.Patient (
                id = patients.id,
                name = patients.name,
                birthday = patients.birthday,
                years = patients.years,
                months = patients.months,
                gender = patients.gender,
                fur = patients.fur,
                food_consumer = patients.food_consumer,
                is_heat = patients.is_heat,
                is_pedigree = patients.is_pedigree,
                is_reproductive = patients.is_reproductive,
                is_castrated = patients.is_castrated,
                pathologies = patients.pathologies,
                photo = patients.photo,
                chip = patients.chip,
                aggresive = patients.aggresive,
                is_dead = patients.is_dead,
                specie = patients.specie,
                breed = patients.breed,
                client = patients.client
            )
        )

    return list_patients

def get_patient(patient_id: int):
    patient = PatientModel.filter(PatientModel.id == patient_id).first()

    if not patient:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'patient not found'
        )

    return patient_schema.Patient (
        id = patient.id,
        name = patient.name,
        birthday = patient.birthday,
        years = patient.years,
        months = patient.months,
        gender = patient.gender,
        fur = patient.fur,
        food_consumer = patient.food_consumer,
        is_heat = patient.is_heat,
        is_pedigree = patient.is_pedigree,
        is_reproductive = patient.is_reproductive,
        is_castrated = patient.is_castrated,
        pathologies = patient.pathologies,
        photo = patient.photo,
        chip = patient.chip,
        aggresive = patient.aggresive,
        is_dead = patient.is_dead,
        specie = patient.specie,
        breed = patient.breed,
        client = patient.client
    )

def update_patient(patient_id: int,
    name: str = None,
    birthday: int = None,
    years: int = None,
    months: int = None,
    gender: str = None,
    fur: str = None,
    food_consumer: str = None,
    is_heat: bool = None,
    is_pedigree: bool = None,
    is_reproductive: bool = None,
    is_castrated: bool = None,
    pathologies: str = None,
    photo: str = None,
    chip: str = None,
    aggresive: float = None,
    is_dead: bool = None,
    specie: int = None,
    breed: int = None,
    client: int = None
):
    patient = PatientModel.filter(PatientModel.id == patient.id).fist()

    if not patient:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Patien not found'
        )

    patient.name = name or patient.name
    patient.birthday = birthday or patient.birthday
    patient.years = years or patient.years
    patient.months = months or patient.months
    patient.gender = gender or patient.gender
    patient.fur = fur or patient.fur
    patient.food_consumer = food_consumer or patient.food_consumer
    patient.is_heat = is_heat or patient.is_heat
    patient.is_pedigree = is_pedigree or patient.is_pedigree
    patient.is_reproductive = is_reproductive or patient.is_reproductive
    patient.is_castrated = is_castrated or patient.is_castrated
    patient.pathologies = pathologies or patient.pathologies
    patient.photo = photo or patient.photo
    patient.chip = chip or patient.chip
    patient.aggresive = aggresive or patient.aggresive
    patient.is_dead = is_dead or patient.is_dead
    patient.specie = specie or patient.specie
    patient.breed = breed or patient.breed
    patient.client = client or patient.client

    patient.save()

    return patient_schema.Patient(
        id = patient.id,
        name = patient.name,
        birthday = patient.birthday,
        years = patient.years,
        months = patient.months,
        gender = patient.gender,
        fur = patient.fur,
        food_consumer = patient.food_consumer,
        is_heat = patient.is_heat,
        is_pedigree = patient.is_pedigree,
        is_reproductive = patient.is_reproductive,
        is_castrated = patient.is_castrated,
        pathologies = patient.pathologies,
        photo = patient.photo,
        chip = patient.chip,
        aggresive = patient.aggresive,
        is_dead = patient.is_dead,
        specie = patient.specie,
        breed = patient.breed,
        client = patient.client
    )

def delete_patient(patient_id: int):
    patient = PatientModel(PatientModel.id == patient_id).first()

    if not patient:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Patien not found'
        )
    
    patient.delete_instance()
