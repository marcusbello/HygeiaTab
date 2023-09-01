import { MedicalRecord } from "./medical-record";

export interface User {
    email:           string;
    first_name:      string;
    last_name:       string;
    gender:          string;
    dob:             Date;
    id:              number;
    is_active:       boolean;
    medical_records: MedicalRecord[];
}
