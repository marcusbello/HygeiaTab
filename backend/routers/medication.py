from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import schema
from database import get_db
from oauth2 import get_current_user
from repository import medication

router = APIRouter(
    prefix="/medication",
    tags=['Medications']
)


@router.get("/{medication_id}", response_model=schema.Medication)
def get_medication(medication_id: int, db: Session = Depends(get_db), current_user: schema.Patient = Depends(get_current_user)):
    return medication.get_medication(medication_id=medication_id, db=db, current_user=current_user)


@router.put("/{medication_id}", response_model=schema.Medication)
def update_medication(medication_id: int, data: schema.Medication, db: Session = Depends(get_db), current_user: schema.Patient = Depends(get_current_user)):
    return medication.update_medication(medication_id=medication_id, data=data, db=db, current_user=current_user)


@router.delete("/{medication_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medication(medication_id: int, db: Session = Depends(get_db), current_user: schema.Patient = Depends(get_current_user)):
    return medication.delete_medication(medication_id=medication_id, db=db, current_user=current_user)
