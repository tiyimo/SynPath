import datetime

# Interactions for diabetes maternity related services
# "specialist_ant_advice",
# "pregnancy_advice"

# Diabetes interaction 20: Specialist antenatal advice
# Appointments for advice within a specialist antenatal service

def specialist_ant_advice(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "specialist antenatal advice",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "specialist antenatal advice", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 112, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 15: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        15: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 21: Maternity care
# Appointments for maternity care

def maternity_care(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "maternity care",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "maternity care", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 58, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 15: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        15: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )