from app.v1.model.user_model import User
from app.v1.model.todo_model import Todo
from app.v1.model.appointment_model import Appointment
from app.v1.model.breed_model import Breed
from app.v1.model.client_model import Client
from app.v1.model.clinic_model import Clinic
from app.v1.model.consultation_model import Consultation
from app.v1.model.detail_purchase_model import DetailPurchase
from app.v1.model.detail_sale_model import DetailSale
from app.v1.model.dewormer_model import Dewormer
from app.v1.model.esthetic_has_type_service_model import EstheticHasTypeService
from app.v1.model.esthetic_model import Esthetic
from app.v1.model.hospitalization_model import Hospitalization
from app.v1.model.laboratory_model import Laboratory
from app.v1.model.patient_model import Patient
from app.v1.model.pet_daycare_model import PetDaycare
from app.v1.model.product_category_model import ProductCategory
from app.v1.model.product_model import Product
from app.v1.model.provider_model import Provider
from app.v1.model.purchase_model import Purchase
from app.v1.model.sale_model import Sale
from app.v1.model.species_model import Species
from app.v1.model.type_appointment_model import TypeAppointment
from app.v1.model.type_dewormer_model import TypeDewormer
from app.v1.model.type_service_model import TypeService
from app.v1.model.type_vaccine_model import TypeVaccine
from app.v1.model.vaccine_model import Vaccine

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([
            User,
            Todo,
            TypeAppointment,
            TypeDewormer,
            TypeService,
            TypeVaccine,
            Vaccine,
            Appointment,
            Breed,
            Client,
            Clinic,
            Consultation,
            DetailPurchase,
            DetailSale,
            Dewormer,
            EstheticHasTypeService,
            Esthetic,
            Hospitalization,
            Laboratory,
            Patient,
            PetDaycare,
            ProductCategory,
            Product,
            Provider,
            Purchase,
            Sale,
            Species

        ])
