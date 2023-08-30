import { Medication } from "./medication";
import { Treatment } from "./treatment";

export interface MedicalRecord {
  record_date:         Date;
  record_type:         string;
  healthcare_provider: string;
  description:         string;
  diagnosis:           string;
  symptoms:            string;
  attachments:         any[];
  id:                  number;
  patient_id:          number;
  treatments:          Treatment[];
  medications:         Medication[];
}