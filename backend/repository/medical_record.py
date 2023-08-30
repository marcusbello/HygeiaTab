import logging

from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
import schema
from database import get_db
from schema import MedicalRecordCreate, Patient

import models


def get_all(patient: Patient, db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.MedicalRecord).filter(models.MedicalRecord.patient == patient).offset(skip).limit(
        limit).all()


def create(data: MedicalRecordCreate, patient: Patient, db: Session):
    medical_record = models.MedicalRecord(**data.dict(), patient_id=patient.id)
    db.add(medical_record)
    db.commit()
    db.refresh(medical_record)
    return medical_record


def get_medical_record(medical_record_id: int, db: Session):
    return db.query(models.MedicalRecord).filter(models.MedicalRecord.id == medical_record_id).first()


def get_medical_record_by_patient(medical_record_id: int, db: Session, patient: Patient):
    return db.query(models.MedicalRecord).filter(
        models.MedicalRecord.id == medical_record_id and models.MedicalRecord.patient == patient).first()


def update_medical_record(medical_record_id: int,
                          data: schema.MedicalRecord,
                          db: Session,
                          current_user: Patient):
    medical_record = db.query(models.MedicalRecord).filter(models.MedicalRecord.id == medical_record_id)
    if not medical_record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Record with id {medical_record_id} is not found')
    model = medical_record.first()
    if model.patient_id != current_user.id:
        raise HTTPException(status_code=401, detail='Unauthorised request')
    medical_record.update(**data.dict())
    db.commit()
    return 'Updated'


def delete_medical_record(medical_record_id: int,
                          current_user: Patient,
                          db: Session = Depends(get_db),
                          ):
    medical_record = db.query(models.MedicalRecord).filter(models.MedicalRecord.id == medical_record_id)
    if not medical_record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Record with id {medical_record_id} is not '
                                                                          f'found')
    model = medical_record.first()
    if model.patient_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Unauthorised requests')
    medical_record.delete(synchronize_session=False)
    db.commit()
    return 'Done'
