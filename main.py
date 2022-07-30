from fastapi import FastAPI

from app.v1.router.user_router import router as user_router
from app.v1.router.todo_router import router as todo_router
from app.v1.router.appointment_router import router as appointment_router
from app.v1.router.breed_router import router as breed_router
from app.v1.router.client_router import router as client_router
from app.v1.router.clinic_router import router as clinic_router
from app.v1.router.consultation_router import router as consultation_router
from app.v1.router.detail_purchase_router import router as detail_purchase_router
from app.v1.router.detail_sale_router import router as detail_sale_router
from app.v1.router.esthetic_has_type_service_router import router as esthetic_has_type_service_router
from app.v1.router.esthetic_router import router as esthetic_router
from app.v1.router.dewormer_router import router as dewormer_router
from app.v1.router.hospitalization_router import router as hospitalization_router
from app.v1.router.laboratory_router import router as laboratory_router
from app.v1.router.patient_router import router as patient_router
from app.v1.router.pet_daycare_router import router as pet_daycare_router
from app.v1.router.product_category_router import router as product_category_router
from app.v1.router.product_router import router as product_router
from app.v1.router.provider_router import router as provider_router
from app.v1.router.purchase_router import router as purchase_router
from app.v1.router.sale_router import router as sale_router
from app.v1.router.species_router import router as species_router
from app.v1.router.type_appointment_router import router as type_appointment_router
from app.v1.router.type_dewormer_router import router as type_dewormer_router
from app.v1.router.type_service_router import router as type_service_router
from app.v1.router.type_vaccine_router import router as type_vaccine_router
from app.v1.router.vaccine_router import router as vaccine_router

app = FastAPI()

app.include_router(user_router)
app.include_router(todo_router)
app.include_router(appointment_router)
app.include_router(breed_router)
app.include_router(client_router)
app.include_router(clinic_router)
app.include_router(consultation_router)
app.include_router(detail_purchase_router)
app.include_router(detail_sale_router)
app.include_router(esthetic_has_type_service_router)
app.include_router(esthetic_router)
app.include_router(dewormer_router)
app.include_router(hospitalization_router)
app.include_router(laboratory_router)
app.include_router(patient_router)
app.include_router(pet_daycare_router)
app.include_router(product_category_router)
app.include_router(provider_router)
app.include_router(product_router)
app.include_router(purchase_router)
app.include_router(sale_router)
app.include_router(species_router)
app.include_router(type_appointment_router)
app.include_router(type_dewormer_router)
app.include_router(type_service_router)
app.include_router(type_vaccine_router)
app.include_router(vaccine_router)
