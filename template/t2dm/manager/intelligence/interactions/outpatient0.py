# Interactions for outpatient care

# "outp_consultation_t2"
# "outp_consultation_ed"
# "laser_treatment"
# "intensive_glucose_control"
# "cvd_risk_reduction"
# "prevent_foot"
# "manage_foot"
# "nutrition_advice"
# "exit_model" (kidney/ liver)


# Diabetes interaction 35: Outpatient consultation in a diabetes service

def outp_consultation_t2(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "diabetes service consultation",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "diabetes service consultation", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 145, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 36: Outpatient consultation (urology) for diabetes related ED

def outp_consultation_ed(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "diabetes-related urology consultation",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "diabetes-related urology consultation", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 105, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 37: Laser eye treatment for diabetes 

def laser_treatment(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "laser treatment",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "laser treatment", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 1081, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 19: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        19: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 38: Intensive glucose control

def intensive_glucose_control(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "intensive glucose control",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "intensive glucose control", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 145,
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Diabetes interaction 39: Cardiovascular disease risk reduction

def cvd_risk_reduction(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "cvd risk reduction",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "cvd risk reduction", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 138, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 40: Preventing foot problems in outpatient services
# Caring for feet with chiropody etc with footcare in outpatient services

def prevent_foot_outpatient(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "footcare prevention in outpatient",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "footcare prevention in outpatient", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 43, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 33: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        33: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Diabetes interaction 41: Managing foot problems in outpatient services
# Managing feet problems such as foot ulcers with footcare in outpatient services

def manage_foot_outpatient(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "footcare management in outpatient",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "footcare management in outpatient", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 54, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 33: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        33: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 42: Nutrition advice from a dietician

def nutrition_advice(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "nutrition advice",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "nutrition advice", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "cost": 90, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 27: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        27: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 43: Kidney specialist # change to exit model

def kidney_specialist(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "kidney specialist",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "kidney specialist", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 1} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 43: Liver specialist # change to exit model

def liver_specialist(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "liver specialist",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "liver specialist", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 1} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )