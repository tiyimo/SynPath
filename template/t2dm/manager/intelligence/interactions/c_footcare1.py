import datetime

# Interactions for diabetes footcare
# "prevent_foot_community",
# "manage_foot_community"

# Diabetes interaction 23: Preventing foot problems in the community
# Caring for feet with chiropody etc with footcare in the community

def prevent_foot_community(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "footcare prevention in community",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "footcare prevention in community", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 43, # NHS Ref costs
        "glucose": -1
        "carbon": 25 # update for more accurate figure
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 26: 0.2, 34: 0.3} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        26: datetime.timedelta(days=20),
        34: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Diabetes interaction 24: Managing foot problems in the community
# Caring for feet problems such as foot ulcers with footcare in the community

def manage_foot_community(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "footcare management in community",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "footcare management in community", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 54, # NHS Ref costs
        "glucose": -1
        "carbon": 25 # update for more accurate figure
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {2: 0.5, 26: 0.2, 34: 0.3} 

    next_environment_id_to_time = {
        2: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        26: datetime.timedelta(days=20),
        34: datetime.timedelta(days=20)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )
