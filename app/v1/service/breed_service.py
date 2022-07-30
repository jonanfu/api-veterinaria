from unicodedata import name
from fastapi import HTTPException, status

from app.v1.schema import breed_shema
from app.v1.model.breed_model import Breed as BreedModel

def create_breed(breed: breed_shema.BreedCreate):
    db_breed = BreedModel(
        name = breed.name,
        description = breed.description,
        species = breed.species
    )

    db_breed.save()

    return breed_shema.Breed(
        id = db_breed.id,
        name = db_breed.name,
        description = db_breed.description,
        species = db_breed.species
    )

def get_breeds():
    breeds = BreedModel.select().order_by(BreedModel.name.desc())

    list_breeds = []

    for breed in breeds:
        list_breeds.append(
            breed_shema.Breed(
                id = breed.id,
                name = breed.name,
                description = breed.description,
                species = breed.species
            )
        )
    
    return list_breeds

def update_breed(breed_id: int, 
    name: str = None,
    description: str = None,
    species: int = None
):
    breed = BreedModel.filter(BreedModel.id == breed_id).first()
    
    if not breed:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Breed not found'
        )
    
    breed.name = name or breed.name
    breed.description = description or breed.description
    breed.species = species or breed.species

    breed.save()

def delete_breed(breed_id: int):
    breed = BreedModel.filter(BreedModel.id == breed_id).first()

    if not breed:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Breed not found'
        )

    breed.delete_instance()
