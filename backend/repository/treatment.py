from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schema


def create_treatment(medical_record_id: int, data: schema.TreatmentCreate, db: Session, current_user: schema.Patient):
    medical_record = db.query(models.MedicalRecord).filter(models.MedicalRecord.id == medical_record_id).first()
    if not medical_record:
        raise HTTPException(status_code=404, detail="Medical record not found")

    treatment = models.Treatment(medical_record_id=medical_record_id, **data.dict())
    db.add(treatment)
    db.commit()
    db.refresh(treatment)
    return treatment


def get_treatments(medical_record_id: int, db: Session, current_user: schema.Patient):
    return db.query(models.Treatment).filter(models.Treatment.medical_record_id == medical_record_id).all()


def get_treatment(treatment_id: int, db: Session, current_user: schema.Patient):
    treatment = db.query(models.Treatment).filter(models.Treatment.id == treatment_id).first()

    if not treatment:
        raise HTTPException(status_code=404, detail="Treatment not found")

    return treatment


def update_treatment(treatment_id: int, data: schema.Treatment, db: Session, current_user: schema.Patient):
    treatment = db.query(models.Treatment).filter(models.Treatment.id == treatment_id)
    if not treatment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Treatment with id {treatment_id} is not found')
    model = treatment.first()
    if model.patient_id != current_user.id:
        raise HTTPException(status_code=401, detail='Unauthorised request')
    treatment.update(**data.dict())
    db.commit()
    return 'Updated'


def delete_treatment(treatment_id: int, db: Session, current_user: schema.Patient):
    treatment = db.query(models.Treatment).filter(models.Treatment.id == treatment_id)
    if not treatment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Record with id {treatment_id} is not '
                                                                          f'found')
    model = treatment.first()
    if model.patient_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Unauthorised requests')
    treatment.delete(synchronize_session=False)
    db.commit()
    return 'Done'

