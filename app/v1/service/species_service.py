from fastapi import HTTPException, status

from app.v1.schema import species_schema
from app.v1.model.species_model import Species as SpeciesModel

def create_species(species: species_schema.SpeciesCreate):
    pass

def get_species():
    pass

def get_species_by_id(species_id: int):
    pass

def update_species(species_id: int, species: species_schema.SpeciesUpdate):
    pass

def delete_species(species_id: int):
    pass

