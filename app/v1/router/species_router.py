from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import species_schema
from app.v1.service import species_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/species')


@router.post (
    '/',
    tags = ['species'],
    status_code = status.HTTP_201_CREATED,
    response_model = species_schema.Species,
    dependencies = [Depends(get_db)]
)
def create_species (
    species: species_schema.SpeciesCreate = Body(...)):
    return species_service.create_species(species)


@router.get (
    '/',
    tags = ['species'],
    status_code = status.HTTP_200_OK,
    response_model = List[species_schema.Species],
    dependencies = [Depends(get_db)]
)
def get_species():
    return species_service.get_species()


@router.get (
    '/{species_id}',
    tags = ['species'],
    status_code = status.HTTP_200_OK,
    response_model = species_schema.Species,
    dependencies = [Depends(get_db)]
)
def get_species(
    species_id: int = Path (
        ...,
        gt=0
    )
):
    return species_service.get_species(species_id)


@router.patch (
    '/{species_id}/update',
    tags = ['species'],
    status_code = status.HTTP_200_OK,
    response_model = species_schema.Species,
    dependencies=[Depends(get_db)]
)
def species_update (
    species_id: int = Path(
        ...,
        gt=0
    ),
    species: species_schema.Species = Body(...)
):
    return species_service.update_species(species_id,
        name = species.name,
        description = species.description
        ) 


@router.delete(
    "/{species_id}/",
    tags=["species"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_species(
    species_id: int = Path(
        ...,
        gt=0
    ),
    current_user: User = Depends(get_current_user)
):
    species_service.delete_species(species_id)

    return {
        'msg': 'species has been deleted sucessfully'
    }
