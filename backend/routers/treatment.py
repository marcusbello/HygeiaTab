from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import schema
from database import get_db
from oauth2 import get_current_user
from repository import treatment

router = APIRouter(
    prefix="/treatment",
    tags=['Treatments']
)


@router.get("/{treatment_id}", response_model=schema.Treatment)
def get_treatment(treatment_id: int, db: Session = Depends(get_db), current_user: schema.Patient = Depends(get_current_user)):
    return treatment.get_treatment(treatment_id=treatment_id, db=db, current_user=current_user)


@router.put("/{treatment_id}", response_model=schema.Treatment)
def update_treatment(treatment_id: int, data: schema.Treatment, db: Session = Depends(get_db), current_user: schema.Patient = Depends(get_current_user)):
    return treatment.update_treatment(treatment_id=treatment_id, data=data, db=db, current_user=current_user)


@router.delete("/{treatment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_treatment(treatment_id: int, db: Session = Depends(get_db), current_user: schema.Patient = Depends(get_current_user)):
    return treatment.delete_treatment(treatment_id=treatment_id, db=db, current_user=current_user)
