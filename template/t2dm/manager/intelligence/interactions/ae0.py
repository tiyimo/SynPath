import datetime

# Interactions for A&E
# "initial diagnosis",
# "acute_event_tr"

# Diabetes interaction 26: A&E diagnosis 

def initial_diagnosis(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "initial diagnosis",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "initial diagnosis", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 166, # NHS reference costs
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 8: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
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

# Diabetes interaction 27: A&E treatment 

def acute_event_tr(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "acute event treatment",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "acute event treatment", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 166, # NHS reference costs
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 8: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
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