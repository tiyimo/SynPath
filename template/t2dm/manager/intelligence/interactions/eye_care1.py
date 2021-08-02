 import datetime
 
# Interactions for eye care services in the community
# "retinopathy_screening"

# Diabetes interaction 20: Retinopathy service
# Appointments for advice within a specialist antenatal service

def retinopathy_screening(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "retinopathy screening",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "retinopathy screening", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 74, # NHS Ref costs
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 8: 0.5} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        8: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )