from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.species_model import Species

#tabla raza
class Breed(BaseModel):
    name = CharField()
    description = CharField()

    species = ForeignKeyField(Species, backref = 'species')
