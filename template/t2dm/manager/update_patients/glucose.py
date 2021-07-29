# Paranjape's model for simulating movement of glucose levels in patients.
# Wu's model of diabetes type 2 glucose cycles: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC546416/#S1

# Simple version: 10% of prediabetic (medium glucose) patients becoming diabetes (high glucose) patients each year
# At the moment just at year 1, but tbc so it happens every year.

import datetime

hba1c = patients.patient_hba1c # refer to the inputs from the patient json.

def glucose_update(patient, patient_time):
 
   entry = {
        "resource_type": "Condition",
        "name": "glucose",
        "start": "patient_time",
   } 
        
    new_patient_record_entries = [entry, glucose_update]

    glucose_update_to_prob = {"medium": 0.90, "high": 0.10}

    for patient in patient(range(10000)):
        if hba1c == "medium" & patient_time==datetime.timedelta(years=1):
            update_data = {"new_patient_record_entries": new_patient_record_entries}
            return (
            patient,
            update_data,
            glucose_update_to_prob,
            )