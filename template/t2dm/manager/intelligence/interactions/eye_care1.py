import datetime
 
# Interactions for eye care services in the community
# "retinopathy_screening"

# Eye care interaction 1: Retinopathy service
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
        "glucose": 0,
        "carbon": 25, # update for more accurate figure
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {24: 0.5, 28: 0.5} # afilbercept and inpatient for retinal procedure

    next_environment_id_to_time = {
        24: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
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

# Eye care interaction 2: Afilbercept (high cost drug)
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
        "glucose": 0,
        "carbon": 25, # update for more accurate figure
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 28: 0.5} # gp and inpatient for retinal procedure

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