# Reads in the initial value (currentSmoker)
# Chance of becoming a smoker of 0.05
# Chance of stopping smoking of 0.1 if you are just running through the model
# Chance of stopping smoking of 0.3 if you run through the smoking cessation service

import datetime

# 10% chance of stopping smoking just running through the model:

def smoking_update(patient, patient_time):
 
   entry = {
        "resource_type": "Condition",
        "name": "stop_smoking",
        "start": patient_time,
        "patient.patient_currentSmoker": "Y",
    } 

    new_patient_record_entries = [entry]

    stop_smoking_to_prob = {0: 0.1, 1: 0.9}

    for patient in patient(range(10000)):
        if "patient.patient_currentSmoker" == 1:
            update_data = {"new_patient_record_entries": new_patient_record_entries}
            return (
                patient,
                update_data,
                stop_smoking_to_prob,
            )