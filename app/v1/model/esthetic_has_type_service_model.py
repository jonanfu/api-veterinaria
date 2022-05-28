from peewee import *

from app.v1.model.base_model import BaseModel
from app.v1.model.esthetic_model import Esthetic
from app.v1.model.type_service_model import TypeService

#tabla estetica tiene tipo de servicio
class EstheticHasTypeService(BaseModel):
    esthetic = ForeignKeyField(Esthetic, backref = 'esthetic_has_type_service')
    type_service = ForeignKeyField(TypeService, backref = 'esthetic_has_type_service')
