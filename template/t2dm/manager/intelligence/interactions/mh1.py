import datetime

# Diabetes interaction 17: Psychological assessment

def psychol_assessment(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "psychological assessment",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "psychological assessment", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 96, # NHS Ref cost for IAPT - PSSRU
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

# Diabetes interaction 18: IAPT

def iapt(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "iapt",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "iapt", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 96, # NHS Ref cost for IAPT - PSSRU
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


# Diabetes interaction 19: Community mental health for severe mental illness

def cmh_for_smi(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "cmh for smi",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "cmh for smi", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 96, # NHS Ref cost for IAPT - PSSRU
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
