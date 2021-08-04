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

import datetime

# Outpatient interaction 1: Outpatient consultation in a diabetes service

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
        "glucose": -1,
        "carbon": 22, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 29: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Outpatient interaction 2: Outpatient consultation (urology) for diabetes related ED

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
        "glucose": 0,
        "carbon": 22, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 29: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Outpatient interaction 3: Laser eye treatment for diabetes 

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
        "glucose": 0,
        "carbon": 300,  
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 23: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        23: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Outpatient interaction 4: Intensive glucose control

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
        "glucose": -1,
        "carbon": 22, 
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 29: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Outpatient interaction 5: Cardiovascular disease risk reduction

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
        "glucose": 0,
        "carbon": 22,  
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 29: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Outpatient interaction 6: Preventing foot problems in outpatient services
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
        "glucose": 0,
        "carbon": 22,  
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 35: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        35: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Outpatient interaction 7: Managing foot problems in outpatient services
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
        "glucose": 0,
        "carbon": 22,  
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 35: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        35: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Outpatient interaction 8: Nutrition advice from a dietician

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
        "glucose": 0,
        "carbon": 22,  
    }

    new_patient_record_entries = [encounter, entry]

    next_environment_id_to_prob = {0: 0.5, 29: 0.5} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        29: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Outpatient interaction 9: Kidney specialist # change to exit model

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

# Outpatient interaction 10: Liver specialist # change to exit model
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