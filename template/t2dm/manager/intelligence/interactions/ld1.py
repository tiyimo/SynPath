import datetime

# Interaction for patient with learning disabilities
# "adj_to_care"

# Learning disability interaction 1: Adjustments to care
# This can mean adjusting lifestyle education so that it meets the needs of people with learning disabilities

def adj_to_care(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "ld_service",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "ld_service", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 200, # update for accurate cost
    }

    new_patient_record_entries = [encounter, adj_to_care]

    next_environment_id_to_prob = {2: 0.5, 6: 0.5} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        6: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )
