from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import repository
import schema
from database import get_db
from oauth2 import get_current_user
from schema import MedicalRecordCreate, MedicalRecord, Patient
from repository import medical_record, treatment, medication

router = APIRouter(
    prefix="/medical-record",
    tags=['Medical Records']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=MedicalRecord)
def create_medical_record(data: MedicalRecordCreate,
                          db: Session = Depends(get_db),
                          current_user: Patient = Depends(get_current_user),
                          ):
    """

    :param data:
    :param db:
    :param current_user:
    :return:
    """
    return medical_record.create(data=data, db=db, patient=current_user)


@router.get('/', response_model=List[MedicalRecord])
async def get_medical_records(db: Session = Depends(get_db),
                              current_user: Patient = Depends(get_current_user),
                              skip: int = 0,
                              limit: int = 100,
                              ):
    """

    :param db:
    :param current_user:
    :param skip:
    :param limit:
    :return:
    """
    return medical_record.get_all(patient=current_user, db=db, skip=skip, limit=limit)


@router.get('/{medical_record_id}', response_model=MedicalRecord)
async def get_medical_record(medical_record_id: int,
                             db: Session = Depends(get_db),
                             current_user: Patient = Depends(get_current_user)):
    """

    :param medical_record_id:
    :param db:
    :param current_user:
    :return:
    """
    return medical_record.get_medical_record_by_patient(medical_record_id=medical_record_id,
                                                        db=db,
                                                        patient=current_user)


@router.put('/{medical_record_id}', status_code=status.HTTP_202_ACCEPTED)
def update_medical_record(medical_record_id: int,
                          data: MedicalRecord,
                          db: Session = Depends(get_db),
                          current_user: Patient = Depends(get_current_user)):
    """

    :param medical_record_id:
    :param data:
    :param db:
    :param current_user:
    :return:
    """
    return medical_record.update_medical_record(medical_record_id=medical_record_id,
                                                data=data,
                                                db=db, current_user=current_user)


@router.delete('/{medical_record_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_record(medical_record_id: int,
                          db: Session = Depends(get_db),
                          current_user: Patient = Depends(get_current_user)):
    """

    :param medical_record_id:
    :param db:
    :param current_user:
    :return:
    """
    return medical_record.delete_medical_record(medical_record_id=medical_record_id,
                                                current_user=current_user,
                                                db=db)


@router.post("/{medical_record_id}/treatment", status_code=201, response_model=schema.Treatment)
def create_treatment(medical_record_id: int,
                     data: schema.TreatmentCreate,
                     db: Session = Depends(get_db),
                     current_user: Patient = Depends(get_current_user)):
    """

    :param medical_record_id:
    :param data:
    :param db:
    :param current_user:
    :return:
    """
    return treatment.create_treatment(medical_record_id, data, db, current_user)


@router.get("/{medical_record_id}/treatments", response_model=List[schema.Treatment])
def get_treatments(medical_record_id: int,
                   db: Session = Depends(get_db),
                   current_user: Patient = Depends(get_current_user)):
    """

    :param medical_record_id:
    :param db:
    :param current_user:
    :return:
    """
    return treatment.get_treatments(medical_record_id, db, current_user)


@router.post("/{medical_record_id}/medication", status_code=201, response_model=schema.Medication)
def create_medication(medical_record_id: int,
                      data: schema.MedicationCreate,
                      db: Session = Depends(get_db),
                      current_user: Patient = Depends(get_current_user)):
    """

    :param medical_record_id:
    :param data:
    :param db:
    :param current_user:
    :return:
    """
    return medication.create_medication(medical_record_id, data, db, current_user)


@router.get("/{medical_record_id}/medication", response_model=List[schema.Medication])
def get_medications(medical_record_id: int,
                    db: Session = Depends(get_db),
                    current_user: Patient = Depends(get_current_user)):
    """

    :param medical_record_id:
    :param db:
    :param current_user:
    :return:
    """
    return medication.get_medications(medical_record_id, db, current_user)
