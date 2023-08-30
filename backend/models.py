
from sqlalchemy import Integer, Column, Date, String, Enum as EnumDB, Boolean, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from database import Base
from schema import Gender, MedicalRecordType, TreatmentType, DosageForm


class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True, index=True)
    record_date = Column(Date)
    record_type = Column(EnumDB(MedicalRecordType))
    healthcare_provider = Column(String)
    description = Column(String)
    diagnosis = Column(String)
    symptoms = Column(String)
    # consent_authorization = Column(String) # change to enum or boolean
    attachments = Column("attachments", ARRAY(String))
    patient_id = Column(Integer, ForeignKey('patients.id'))

    patient = relationship("Patient", back_populates="medical_records")
    treatments = relationship("Treatment", back_populates="medical_record")
    medications = relationship("Medication", back_populates="medical_record")


class Treatment(Base):
    __tablename__ = 'treatments'

    id = Column(Integer, primary_key=True, index=True)
    treatment_title = Column(String)
    treatment_type = Column(EnumDB(TreatmentType))
    treatment_date = Column(Date)
    treatment_provider = Column(String)
    diagnosis = Column(String)
    description = Column(String)
    dosage = Column(String)
    frequency = Column(String)
    duration = Column(String)
    follow_up_instructions = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    medical_record_id = Column(Integer, ForeignKey('medical_records.id'))
    medical_record = relationship("MedicalRecord", back_populates="treatments")


class Medication(Base):
    """

    """
    __tablename__ = 'medications'

    id = Column(Integer, primary_key=True, index=True)
    medication_name = Column(String)
    medication_type = Column(String)
    dosage_form = Column(EnumDB(DosageForm))
    strength = Column(String)
    dosage_instructions = Column(String)
    prescribing_doctor = Column(String)
    prescription_date = Column(Date)
    dispensing_pharmacy = Column(String)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    refills = Column(Integer, nullable=True)
    indications = Column(String)
    side_effects = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    medical_record_id = Column(Integer, ForeignKey('medical_records.id'))
    medical_record = relationship("MedicalRecord", back_populates="medications")


class Patient(Base):
    """

    """
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    gender = Column(EnumDB(Gender), default='Other')
    hashed_password = Column(String)
    dob = Column(Date)
    is_active = Column(Boolean, default=True)

    medical_records = relationship("MedicalRecord", back_populates='patient')
