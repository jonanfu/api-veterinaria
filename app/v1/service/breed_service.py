from fastapi import HTTPException, status

from app.v1.schema import breed_shema
from app.v1.model.breed_model import Breed as BreedModel

def create_breed(breed: breed_shema.BreedCreate):
    pass

def get_breeds():
    pass

def update_breed(breed_id: int, breed: breed_shema.BreedUpdate):
    pass

def delete_breed(breed_id: int):
    pass
