from datetime import datetime

from fastapi import HTTPException, status

from app.v1.schema import consultation_schema
from app.v1.schema import user_schema
from app.v1.model import consultation_model as ConsultationModel

def create_consultation(
    consultation: consultation_schema.ConsultationCreate,
    user: user_schema.User
):
    db_consultation = ConsultationModel(
        date = consultation.date,
        reason_visit = consultation.reason_visit,
        anommesis = consultation.anommesis,
        physical_exam = consultation.physical_exam,
        diagnosis = consultation.diagnosis,
        pathology = consultation.pathology,
        treatment = consultation.treatment,
        recipe = consultation.recipe,
        price = consultation.price,
        send_whatsapp = consultation.send_whatsapp,
        send_email = consultation.send_email,
        send_sms = consultation.send_sms,
        form_payment = consultation.form_payment,
        is_paid = consultation.is_paid,

        user = user.id,
        vaccine = consultation.vaccine,
        dewormer = consultation.dewormer,
        patient = consultation.patient

    )

    db_consultation.save()

    return consultation_schema.Consultation(
        id = db_consultation.id,
        date = db_consultation.date,
        reason_visit = db_consultation.reason_visit,
        anommesis = db_consultation.anommesis,
        physical_exam = db_consultation.physical_exam,
        diagnosis = db_consultation.diagnosis,
        pathology = db_consultation.pathology,
        treatment = db_consultation.treatment,
        recipe = db_consultation.recipe,
        price = db_consultation.price,
        send_whatsapp = db_consultation.send_whatsapp,
        send_email = db_consultation.send_email,
        send_sms = db_consultation.send_sms,
        form_payment = db_consultation.form_payment,
        is_paid = db_consultation.is_paid,
        created_at = db_consultation.created_at,
        user = db_consultation.id,
        vaccine = db_consultation.vaccine,
        dewormer = db_consultation.dewormer,
        patient = db_consultation.patient
    )
    

def get_consultations_by_user(user: user_schema.User):
    consultations = ConsultationModel.filter(ConsultationModel.user_id == user.id).order_by(ConsultationModel.created_at.desc())

    list_consultations = []
    for consultation in consultations:
        list_consultations.append(
            consultation_schema.Consultation(
                id = consultation.id,
                date = consultation.date,
                reason_visit = consultation.reason_visit,
                anommesis = consultation.anommesis,
                physical_exam = consultation.physical_exam,
                diagnosis = consultation.diagnosis,
                pathology = consultation.pathology,
                treatment = consultation.treatment,
                recipe = consultation.recipe,
                price = consultation.price,
                send_whatsapp = consultation.send_whatsapp,
                send_email = consultation.send_email,
                send_sms = consultation.send_sms,
                form_payment = consultation.form_payment,
                is_paid = consultation.is_paid,
                created_at = consultation.created_at,
                user = consultation.id,
                vaccine = consultation.vaccine,
                dewormer = consultation.dewormer,
                patient = consultation.patient
            )
        )

        return list_consultations

def get_consultation(consultation_id: int):
    consultation = ConsultationModel.filter(ConsultationModel.id == consultation_id).first()

    if not consultation:
        raise HTTPException (
            status_code= status.HTTP_404_NOT_FOUND,
            detail = 'Consultation not found'
        )
    
    return consultation_schema.Consultation (
        id = consultation.id,
        date = consultation.date,
        reason_visit = consultation.reason_visit,
        anommesis = consultation.anommesis,
        physical_exam = consultation.physical_exam,
        diagnosis = consultation.diagnosis,
        pathology = consultation.pathology,
        treatment = consultation.treatment,
        recipe = consultation.recipe,
        price = consultation.price,
        send_whatsapp = consultation.send_whatsapp,
        send_email = consultation.send_email,
        send_sms = consultation.send_sms,
        form_payment = consultation.form_payment,
        is_paid = consultation.is_paid,
        created_at = consultation.created_at,
        user = consultation.id,
        vaccine = consultation.vaccine,
        dewormer = consultation.dewormer,
        patient = consultation.patient
    )

# def get_consultations_by_patient(patient_id: int,

# ):
#     pass

def update_consultation(
    consultation_id: int,
    date:datetime = None,
    reason_visit:str = None,
    anommesis:str = None,
    physical_exam:str = None,
    diagnosis:str = None,
    pathology:str = None,
    treatment:str = None,
    recipe:str = None,
    price:float = None,
    send_whatsapp:bool = None,
    send_email:bool = None,
    send_sms:bool = None,
    form_payment:str = None,
    is_paid:bool = None,
    user:int = None,
    vaccine:int = None,
    dewormer:int = None,
    patient:int = None
):
    consultation = ConsultationModel.filter(ConsultationModel.id == consultation_id).first()

    if not consultation:
        raise HTTPException (
            status_code= status.HTTP_404_NOT_FOUND,
            detail = 'Consultation not found'
        )
    
    consultation.date = date or consultation.date,
    consultation.reason_visit = reason_visit or consultation.reason_visit,
    consultation.anommesis = anommesis or consultation.anommesis,
    consultation.physical_exam = physical_exam or consultation.physical_exam,
    consultation.diagnosis = diagnosis or consultation.diagnosis,
    consultation.pathology = pathology or consultation.pathology,
    consultation.treatment = treatment or consultation.treatment,
    consultation.recipe = recipe or consultation.recipe,
    consultation.price = price or consultation.price,
    consultation.send_whatsapp = send_whatsapp or consultation.send_whatsapp,
    consultation.send_email = send_email or consultation.send_email,
    consultation.send_sms = send_sms or consultation.send_sms,
    consultation.form_payment = form_payment or consultation.form_payment,
    consultation.is_paid = is_paid or consultation.is_paid,
    consultation.user = user or consultation.user,
    consultation.vaccine = vaccine or consultation.vaccine,
    consultation.dewormer = dewormer or consultation.dewormer,
    consultation.patient = patient or consultation.patient

    consultation.save() 

    return consultation_schema.Consultation (
        id = consultation.id,
        date = consultation.date,
        reason_visit = consultation.reason_visit,
        anommesis = consultation.anommesis,
        physical_exam = consultation.physical_exam,
        diagnosis = consultation.diagnosis,
        pathology = consultation.pathology,
        treatment = consultation.treatment,
        recipe = consultation.recipe,
        price = consultation.price,
        send_whatsapp = consultation.send_whatsapp,
        send_email = consultation.send_email,
        send_sms = consultation.send_sms,
        form_payment = consultation.form_payment,
        is_paid = consultation.is_paid,
        created_at = consultation.created_at,
        user = consultation.id,
        vaccine = consultation.vaccine,
        dewormer = consultation.dewormer,
        patient = consultation.patient
    )

def delete_consultation(consultation_id: int, user: user_schema.User):
    consultation = ConsultationModel.filter(ConsultationModel.id == consultation_id).first()

    if not consultation:
        raise HTTPException (
            status_code= status.HTTP_404_NOT_FOUND,
            detail = 'Consultation not found'
        )
    
    consultation.delete_instance()

