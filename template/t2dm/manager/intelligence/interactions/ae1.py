import datetime

# Interactions for A&E
# "initial diagnosis",
# "acute_event_treatment"

# A&E interaction 1: A&E diagnosis 

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

    next_environment_id_to_prob = {2: 0.5, 28: 0.5} # gp, inpatient

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        28: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# A&E interaction 2: A&E treatment 

def acute_event_treatment(patient, environment, patient_time):
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

    next_environment_id_to_prob = {2: 0.2, 28: 0.8} # gp, inpatient

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        28: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )