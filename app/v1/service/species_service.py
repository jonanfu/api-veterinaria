from fastapi import HTTPException, status

from app.v1.schema import species_schema
from app.v1.model.species_model import Species as SpeciesModel

def create_species(species: species_schema.SpeciesCreate):
    db_species = SpeciesModel(
        name = species.name,
        description = species.description
    )

    db_species.save()

    return species_schema.Species(
        id = db_species.id,
        name = db_species.name,
        description = db_species.description
    )

def get_species():
    species = SpeciesModel.select().order_by(SpeciesModel.id.desc())

    list_species = []
    for specie in species:
        list_species.append (
            species_schema.Species(
                id = specie.id,
                name = specie.name,
                description = specie.desciption
            )
        )
    return list_species

def get_species_by_id(species_id: int):
    specie = SpeciesModel.filter(SpeciesModel.id == species_id).first()

    if not specie:
        raise HTTPException (
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Specie not found"
        )

    return species_schema.Species(
        id = specie.id,
        name = specie.name,
        description = specie.description
    )

def update_species(species_id: int, 
    name: str = None,
    description: str = None    
    ):

    specie = SpeciesModel.filter(SpeciesModel.id == species_id).first()

    if not specie:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Specie not found'
        )
    
    specie.name = name or specie.name
    specie.description = description or specie.description

    specie.save()
    return species_schema.Species(
        id = specie.id,
        name = specie.name,
        description = specie.description

    )
def delete_species(species_id: int):
    specie = SpeciesModel.filter(SpeciesModel.id == species_id).first()

    if not specie:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Specie not found'
        )

    specie.delete_instance()
