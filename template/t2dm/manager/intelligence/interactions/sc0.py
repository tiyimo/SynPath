# Diabetes interaction 22: Smoking cessation
# For people who smoke (Y), 20% chance of successfully stopping smoking if they go to the service
# Don't need an if statement as they should only be referred here if they smoke

import datetime

def smoking_cessation1(patient, patient_time):
   encounter = {
       "resource_type": "Encounter",
       "name": "Smoking cessation service",
       "start": patient_time,
   }

   entry = {
        "resource_type": "Condition",
        "name": "stop_smoking",
        "start": patient_time,
        "cost": 143, # if male, 138 if female
    } 

    new_patient_record_entries = [encounter, entry]

    stop_smoking_to_prob = {"Y": 0.8, "N": 0.2}

    next_environment_id_to_prob = {0: 0.5, 7: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        8: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
            patient,
            update_data,
            stop_smoking_to_prob,
            next_environment_id_to_prob,
            next_environment_id_to_time,
            )