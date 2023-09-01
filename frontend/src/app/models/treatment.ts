export interface Treatment {
    treatment_title:        string;
    treatment_type:         string;
    treatment_date:         Date;
    treatment_provider:     string;
    diagnosis:              string;
    description:            string;
    dosage:                 string;
    frequency:              string;
    duration:               string;
    follow_up_instructions: string;
    id:                     number;
    medical_record_id:      number;
}