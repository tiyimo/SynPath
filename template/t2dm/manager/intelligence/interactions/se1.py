import datetime

# All the interactions for structured education
# "f2f_group_education",
# "ddpp",
# "online_lifestyle"


# Diabetes interaction 13: Face to face group education

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
    }

    new_patient_record_entries = [encounter, f2f_group_education]

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

# Diabetes interaction 14: DDPP

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
    }

    new_patient_record_entries = [encounter, f2f_group_education]

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

# Diabetes interaction 14: Online lifestyle education 
def online_lifestyle(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "f2f group education",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "online lifestyle education", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
    }

    new_patient_record_entries = [encounter, online_lifestyle]

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