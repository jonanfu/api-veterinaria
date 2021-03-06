from fastapi import APIRouter, Depends, Body
from fastapi import status
from fastapi import Query
from fastapi import Path

from typing import List, Optional

from app.v1.schema import breed_shema
from app.v1.service import breed_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

router = APIRouter(prefix = '/api/v1/breed')

@router.post (
    '/',
    tags = ['breed'],
    status_code = status.HTTP_201_CREATED,
    response_model = breed_shema.Breed,
    dependencies = [Depends(get_db)]
)
def create_breed (
    breed: breed_shema.BreedCreate = Body(...),
    ):
    return breed_service.create_breed(breed)


@router.get (
    '/',
    tags = ['breed'],
    status_code = status.HTTP_200_OK,
    response_model = List[breed_shema.Breed],
    dependencies = [Depends(get_db)]
)
def get_breeds():
    return breed_service.get_breeds()


# @router.get (
#     '/{breed_id}',
#     tags = ['breed'],
#     status_code = status.HTTP_200_OK,
#     response_model = breed_shema.Breed,
#     dependencies = [Depends(get_db)]
# )
# def get_breed(
#     breed_id: int = Path (
#         ...,
#         gt=0
#     ),
#     current_user: User = Depends(get_current_user)
# ):
#     return breed_service.get_breed(breed_id, current_user)


@router.put (
    '/{breed_id}',
    tags = ['breed'],
    status_code = status.HTTP_200_OK,
    response_model = breed_shema.Breed,
    dependencies = [Depends(get_db)]
)
def update_breed (
    breed_id: int = Path (
        ...,
        gt=0
    ),
    breed: breed_shema.Breed = Body(...),
):
    return breed_service.update_breed(breed_id, 
        name = breed.name,
        description = breed.description,
        species = breed.species)


@router.delete (
    '/{breed_id}',
    tags = ['breed'],
    status_code = status.HTTP_200_OK,
    dependencies = [Depends(get_db)]
)
def delete_breed (
    breed_id: int = Path (
        ...,
        gt=0
    )
):
    breed_service.delete_breed(breed_id)

    return {
        'msg': 'Breed has been deleted sucessfully'
    }

