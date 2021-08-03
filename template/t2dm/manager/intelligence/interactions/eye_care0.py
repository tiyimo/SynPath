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

    next_environment_id_to_prob = {19: 0.5, 25: 0.5} # 19 for afilbercept and inpatient for retinal procedure

    next_environment_id_to_time = {
        19: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        25: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

def afilbercept_prescription(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "afilbercept prescription",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "afilbercept prescription", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 809, # NHS Ref costs
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 25: 0.5} # 0 for gp and 25 inpatient for retinal procedure

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        25: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )