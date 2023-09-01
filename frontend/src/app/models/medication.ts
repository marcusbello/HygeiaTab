export interface Medication {
    medication_name:     string;
    dosage_form:         string;
    strength:            string;
    dosage_instructions: string;
    prescribing_doctor:  string;
    prescription_date:   Date;
    dispensing_pharmacy: string;
    start_date:          Date;
    end_date:            Date;
    refills:             number;
    side_effects:        string;
    id:                  number;
    medical_record_id:   number;
}