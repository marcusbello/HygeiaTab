from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
import schema
from hashing import Hash


def get_patients(db: Session):
    user = db.query(models.Patient).all()
    return user


def create(request: schema.PatientCreate, db: Session):
    new_user = models.Patient(first_name=request.first_name,
                              last_name=request.last_name,
                              email=request.email,
                              dob=request.dob,
                              hashed_password=Hash.bcrypt(request.password)
                              )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_patient(patient_id: int, db: Session, current_user: schema.Patient):
    if patient_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorised request')
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()


def get_current_patient(db: Session, current_user: schema.Patient):
    return db.query(models.Patient).filter(models.Patient.id == current_user.id).first()


def get_patient_by_email(db: Session, email: str, current_user: schema.Patient):
    if email != current_user.email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorised request')
    return db.query(models.Patient).filter(models.Patient.email == email).first()


def update_patient(patient_id,
                   data: schema.Patient,
                   db: Session,
                   current_user: schema.Patient):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id)
    if patient_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Unauthorised request')
    if not patient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Patient with id {patient_id} is not found')
    patient.update(data.dict(exclude_unset=True, exclude_defaults=True))
    db.commit()
    return 'Updated'


def delete_patient(patient_id: int, db: Session, current_user: schema.Patient):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id)
    if patient.id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Unauthorised request')
    if not patient.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Patient with id {id} is not found')
    patient.delete(synchronize_session=False)
    db.commit()
    return 'Done'
