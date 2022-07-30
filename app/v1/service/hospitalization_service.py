from fastapi import HTTPException, status

from app.v1.schema import hospitalization_schema
from app.v1.schema import patient_schema
from app.v1.model import hospitalization_model as HospitalizationModel


def create_hospitalization(hospitalization: hospitalization_schema.HospitalizationCreate, patient: patient_schema.Patient):
    db_hospitalization = HospitalizationModel(
        diagnosis=hospitalization.diagnosis,
        aspect=hospitalization.aspect,
        weight=hospitalization.weight,
        feeding=hospitalization.feeding,
        observation=hospitalization.observation,
        other_indications=hospitalization.other_indications,
        parameters=hospitalization.parameters
    )

    db_hospitalization.save()

    return hospitalization_schema.Hospitalization(
        id=db_hospitalization.id,
        diagnosis=db_hospitalization.diagnosis,
        aspect=db_hospitalization.aspect,
        weight=db_hospitalization.weight,
        feeding=db_hospitalization.feeding,
        observation=db_hospitalization.observation,
        other_indications=db_hospitalization.other_indications,
        parameters=db_hospitalization.parameters,
        date=db_hospitalization.date
    )


def get_hospitalizations():
    hospitalizations = HospitalizationModel.Select().order_by(
        HospitalizationModel.id.desc())

    list_hospitalizations = []
    for hospitalization in hospitalizations:
        list_hospitalizations.append(
            hospitalization_schema.Hospitalization(
                id=hospitalization.id,
                diagnosis=hospitalization.diagnosis,
                aspect=hospitalization.aspect,
                weight=hospitalization.weight,
                feeding=hospitalization.feeding,
                observation=hospitalization.observation,
                other_indications=hospitalization.other_indications,
                parameters=hospitalization.parameters,
                date=hospitalization.date
            )
        )

    return list_hospitalizations


def get_hospitalization(hospitalization_id: int):
    hospitalization = HospitalizationModel.filter(
        HospitalizationModel.id == hospitalization_id).first()

    if not hospitalization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitalization not found'
        )

    return hospitalization_schema.Hospitalization(
        id=hospitalization.id,
        diagnosis=hospitalization.diagnosis,
        aspect=hospitalization.aspect,
        weight=hospitalization.weight,
        feeding=hospitalization.feeding,
        observation=hospitalization.observation,
        other_indications=hospitalization.other_indications,
        parameters=hospitalization.parameters,
        date=hospitalization.date
    )


def update_hospitalization(hospitalization_id: int,
                           diagnosis: str = None,
                           aspect: str = None,
                           weight: float = None,
                           feeding: str = None,
                           observation: str = None,
                           other_indications: str = None,
                           parameters: str = None
                           ):

    hospitalization = HospitalizationModel.filter(
        HospitalizationModel.id == hospitalization_id).first()

    if not hospitalization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitalization not found'
        )

    hospitalization.diagnosis = diagnosis or hospitalization.diagnosis
    hospitalization.aspect = aspect or hospitalization.aspect
    hospitalization.weight = weight or hospitalization.weight
    hospitalization.feeding = feeding or hospitalization.feeding
    hospitalization.observation = observation or hospitalization.observation
    hospitalization.other_indications = other_indications or hospitalization.other_indications
    hospitalization.parameters = parameters or hospitalization.parameters

    return hospitalization_schema.Hospitalization(
        id=hospitalization.id,
        diagnosis=hospitalization.diagnosis,
        aspect=hospitalization.aspect,
        weight=hospitalization.weight,
        feeding=hospitalization.feeding,
        observation=hospitalization.observation,
        other_indications=hospitalization.other_indications,
        parameters=hospitalization.parameters,
        date=hospitalization.date
    )


def delete_hospitalization(hospitalization_id: int):
    hospitalization = HospitalizationModel.filter(
        HospitalizationModel.id == hospitalization_id).first()

    if not hospitalization:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Hospitalization not found'
        )

    hospitalization.delete_instance()
