
# For women below 50 years, probability of getting being pregnant 2% each year

import datetime

# 2% chance of getting pregnant for a female under 50

def pregnancy(patient, patient_time):
    entry = {
            "resource_type": "Condition",
            "name": "Pregnancy",
            "start": patient_time,
            "end": patient_time + datetime.timedelta(days=270),
            "patient.patient_pregnant": 1,
        } 
         
    new_patient_record_entries = [entry]

    pregnant_to_prob = {0: 0.98, 1: 0.02}

    for patient in patient(range(10000)):
        if patient.gender == "female" and patient_time < patient.birth_date+datetime.timedelta(years=50) and patient.patient_pregnant == 0:
            update_data = {"new_patient_record_entries": new_patient_record_entries}
            return (
                patient,
                update_data,
                pregnant_to_prob,
            )
