from datetime import date
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, EmailStr


class Gender(str, Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class PatientBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    gender: Optional[Gender] = Gender.OTHER
    dob: date


class PatientCreate(PatientBase):
    password: str


class MedicalRecordType(str, Enum):
    GENERAL_RECORD = 'General Record'
    LAB_RESULT = 'Lab Result'
    IMAGING_REPORT = 'Imaging Report'
    PROGRESS_NOTE = 'Progress Note'


class MedicalRecordBase(BaseModel):
    record_date: date
    record_type: Optional[MedicalRecordType] = MedicalRecordType.GENERAL_RECORD
    healthcare_provider: str
    description: str
    diagnosis: str
    symptoms: str
    # consent_authorization: str
    attachments: Optional[List[str]] = []


class TreatmentType(str, Enum):
    MEDICATION = 'Medication'
    SURGERY = 'Surgery'
    THERAPY = 'Therapy'
    PROCEDURE = 'Procedure'


class TreatmentBase(BaseModel):
    treatment_title: str
    treatment_type: Optional[TreatmentType] = TreatmentType.PROCEDURE
    treatment_date: date
    treatment_provider: str
    diagnosis: str
    description: str
    dosage: str
    frequency: str
    duration: str
    follow_up_instructions: str


class Treatment(TreatmentBase):
    id: int
    medical_record_id: int

    # medical_record: MedicalRecord

    class Config:
        orm_mode = True


class TreatmentCreate(TreatmentBase):
    pass


class DosageForm(str, Enum):
    TABLET = 'Tablet'
    CAPSULE = 'Capsule'
    LIQUID = 'Liquid'
    INJECTION = 'Injection'


class MedicationBase(BaseModel):
    medication_name: str
    dosage_form: Optional[DosageForm] = DosageForm.TABLET
    strength: str
    dosage_instructions: str
    prescribing_doctor: str
    prescription_date: date
    dispensing_pharmacy: str
    start_date: date
    end_date: date = None
    refills: int = None
    side_effects: str


class Medication(MedicationBase):
    id: int
    medical_record_id: int

    class Config:
        orm_mode = True


class MedicationCreate(MedicationBase):
    pass


class MedicalRecord(MedicalRecordBase):
    id: int
    patient_id: int

    treatments: Optional[List[Treatment]] = []
    medications: Optional[List[Medication]] = []

    class Config:
        orm_mode = True


class MedicalRecordCreate(MedicalRecordBase):
    pass


class Patient(PatientBase):
    id: int
    is_active: bool

    medical_records: list[MedicalRecord] = []

    class Config:
        orm_mode = True


class Login(BaseModel):
    email: EmailStr
    password: str


class TokenData(BaseModel):
    email: EmailStr
