# Diabetes interaction 22: Smoking cessation
# For people who smoke (Y), 20% chance of successfully stopping smoking if they go to the service
# Don't need an if statement as they should only be referred here if they smoke

import datetime

def smoking_cessation(patient, patient_time):
   encounter = {
       "resource_type": "Encounter",
       "name": "smoking cessation",
       "start": patient_time,
   }

   entry = {
        "resource_type": "Condition",
        "name": "stop_smoking",
        "start": patient_time,
        "cost": 143, # if male, 138 if female
    } 

   new_patient_record_entries = [encounter, entry]

   next_environment_id_to_prob = {2: 0.5, 28: 0.5} 

   next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        28: datetime.timedelta(days=20),
    }

   update_data = {"new_patient_record_entries": new_patient_record_entries}
   return (
            patient,
            update_data,
            next_environment_id_to_prob,
            next_environment_id_to_time,
    )