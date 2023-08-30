import { MedicalRecord } from "./medical-record";

export interface RegisterRequest {
  email:      string;
  first_name: string;
  last_name:  string;
  gender:     string;
  dob:        Date;
  password:   string;
}
  
export interface RegisterResponse {
  email:           string;
  first_name:      string;
  last_name:       string;
  gender:          string;
  dob:             Date;
  id:              number;
  is_active:       boolean;
  medical_records: MedicalRecord[];
}

  
export interface RegisterError {
    error: string;
  }