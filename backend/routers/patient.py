from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from oauth2 import get_current_user
from schema import Patient, PatientCreate
from repository import patient

from database import get_db

router = APIRouter(
    prefix="/patient",
    tags=['Patients']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Patient)
def create_patient(request: PatientCreate, db: Session = Depends(get_db)):
    current_user = models.Patient()
    current_user.email = request.email
    db_user = patient.get_patient_by_email(db, email=request.email, current_user=current_user)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return patient.create(request, db)


@router.get('/{patient_id}', response_model=Patient)
async def get_patient(patient_id: int,
                      db: Session = Depends(get_db),
                      current_user: Patient = Depends(get_current_user)):
    return patient.get_patient(patient_id=patient_id, db=db, current_user=current_user)


@router.get('/me/', response_model=Patient)
async def get_current_patient(
                      db: Session = Depends(get_db),
                      current_user: Patient = Depends(get_current_user)):
    return patient.get_current_patient(db=db, current_user=current_user)


@router.put('/{patient_id}', status_code=status.HTTP_202_ACCEPTED)
def update_patient(patient_id: int,
                   data: Patient,
                   db: Session = Depends(get_db),
                   current_user: Patient = Depends(get_current_user)):
    return patient.update_patient(patient_id=patient_id, data=data, db=db, current_user=current_user)


@router.delete('/{patient_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(patient_id: int,
                   db: Session = Depends(get_db),
                   current_user: Patient = Depends(get_current_user)):
    return patient.delete_patient(patient_id=patient_id, db=db, current_user=current_user)
