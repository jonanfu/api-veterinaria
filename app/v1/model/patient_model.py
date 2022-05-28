from datetime import datetime

from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.species_model import Species
from app.v1.model.breed_model import Breed
from app.v1.model.client_model import Client

class Patient(BaseModel):
    name = CharField()
    birthday = DateTimeField()
    years = IntegerField()
    months = IntegerField()
    gender = CharField()
    fur = CharField()
    food_consumer = CharField()
    is_heat = BooleanField(default = False)
    is_pedigree = BooleanField(default = False)
    is_reproductive = BooleanField(default = False)
    is_castrated = BooleanField(default = False)
    pathologies = CharField()
    photo = CharField()
    chip = CharField()
    aggressive = FloatField()
    is_dead = BooleanField(default = False)

    specie = ForeignKeyField(Species, backref = 'patient')
    breed = ForeignKeyField(Breed, backref = 'patient')
    client = ForeignKeyField(Client, backref = 'patient')
