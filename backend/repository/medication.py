from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schema


def create_medication(medical_record_id: int, data: schema.MedicationCreate, db: Session, current_user: models.Patient):
    medical_record = db.query(models.MedicalRecord).filter(models.MedicalRecord.id == medical_record_id).first()
    if not medical_record:
        raise HTTPException(status_code=404, detail="Medical record not found")

    medication = models.Medication(medical_record_id=medical_record_id, **data.dict())
    db.add(medication)
    db.commit()
    db.refresh(medication)
    return medication


def get_medications(medical_record_id: int, db: Session, current_user: schema.Patient):
    return db.query(models.Medication).filter(models.Medication.medical_record_id == medical_record_id).all()


def get_medication(medication_id: int, db: Session, current_user: schema.Patient):
    medication = db.query(models.Medication).filter(models.Medication.id == medication_id).first()

    if not medication:
        raise HTTPException(status_code=404, detail="Medication not found")

    return medication


def update_medication(medication_id: int, data: schema.Medication, db: Session,
                      current_user: schema.Patient):
    medication = db.query(models.Medication).filter(models.Medication.id == medication_id)
    if not medication.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Medication with id {medication_id} is not found')
    model = medication.first()
    if model.patient_id != current_user.id:
        raise HTTPException(status_code=401, detail='Unauthorised request')
    medication.update(**data.dict())
    db.commit()
    return 'Updated'


def delete_medication(medication_id: int, db: Session, current_user: schema.Patient):
    medication = db.query(models.Medication).filter(models.Medication.id == medication_id)
    if not medication.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Medication with id {medication_id} is not '
                                                                          f'found')
    model = medication_id.first()
    if model.patient_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Unauthorised requests')
    medication.delete(synchronize_session=False)
    db.commit()
    return 'Done'
