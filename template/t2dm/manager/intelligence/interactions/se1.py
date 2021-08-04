import datetime

# All the interactions for structured education
# "f2f_group_education",
# "ddpp",
# "online_lifestyle"

# Structured education interaction 1: Face to face group education

def f2f_group_education(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "f2f group education",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "f2f group education", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 203, # DESMOND RCT
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.8, 30: 0.2} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Structured education interaction 2: DDPP

def ddpp(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "ddpp_course",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "ddpp_course", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 150, # update
        "glucose": -1,
        "carbon": 100, # update 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.8, 30: 0.2} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Structured education interaction 3: Online lifestyle education 
def online_lifestyle(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "online lifestyle education",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "online lifestyle education", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 268, # Liva, Nuffield Trust
        "glucose": -1,
        "carbon": 100, # update 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 30: 0.5} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        30: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )