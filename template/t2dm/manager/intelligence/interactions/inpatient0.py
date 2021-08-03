import datetime

# Interactions for inpatient care
# "review_and_consultation",
# "bd_hypoglycaemic_ep",
# "bd_hyperglycaemic_ep",
# "bd_lower_limb_compl",
# "enhanced_independence",
# "retinal_procedure",
# "amputation"

# Diabetes interaction 28: Inpatient review and consultation (might take out if not in spell) 

def review_and_consultation(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "review and consultation",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "review and consultation", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053, # NEL long stay
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.3, 37: 0.1} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
        37: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 29: Hypoglycaemic episode bed day

def bd_hypoglycaemic_ep(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "hypoglycaemic ep bd",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "hypoglycaemic ep bd", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053, # NEL long stay
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.3, 37: 0.1} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
        37: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 30: Hyperglycaemic episode bed day

def bd_hyperglycaemic_ep(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "hyperglycaemic ep bd",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "hyperglycaemic ep bd", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053, # NEL long stay
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.3, 37: 0.1} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
        37: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 31: Lower limb complications bed day

def bd_lower_limb_ep(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "lower limb ep bd",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "lower limb ep bd", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053, # NEL long stay
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.3, 37: 0.1} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
        37: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 32: Enhanced independence

def enhanced_indep(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "enhanced independence",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "enhanced independence", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053, # update this with correct cost

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.3, 37: 0.1} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
        37: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 33: Retinal procedure

def retinal_procedure(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "retinal procedure",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "retinal procedure", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053, # NEL long stay
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.3, 37: 0.1} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
        37: datetime.timedelta(days=20),

    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )
    
# Diabetes interaction 34: Amputation

def amputation(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "amputation",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "amputation", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 3053, # NEL long stay
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.3, 37: 0.1} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        8: datetime.timedelta(days=20),
        37: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )