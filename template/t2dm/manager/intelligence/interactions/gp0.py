import datetime


# All the interactions at the gp
# "blood_test",
# "medication_change1",
# "medication_change1",
# "insulin_prescription",
# "highrisk_management",
# "exercise_prescription",
# "prediabetes_diagnosis",
# "t2dm_diagnosis",
#  "glucose_management",
#  "annual_health_check",
# "hypertension_management",
# "complications_id_mant",
# "glucose_clinic",
    
# Example (bmi)

def bloodtest_encounter(patient, environment, patient_time):

    # NOTE: entries produced by the interaction functions must have 'name',
    # 'start' and 'resource_type' fields, and only the following
    # resource_types are supported for conversion to FHIR
    #   - Patient
    #   - Encounter
    #   - Condition
    #   - Observation
    #   - Procedure
    #   - MedicationRequest
    #   - ServiceRequest
    #   - Appointment
    # See the patient_abm.data_handler.fhir module for the code that implements
    # the conversion (e.g. the convert_patient_record_entry_to_fhir function)

    entry = {
        "resource_type": "Encounter",
        "name": "blood test encounter",
        "start": patient_time,
    }

    new_patient_record_entries = [entry]

    next_environment_id_to_prob = {0: 0.9, 1: 0.1}

    next_environment_id_to_time = {
        0: datetime.timedelta(days=14),
        1: datetime.timedelta(days=2),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Diabetes interaction 1: blood test, measure hba1c

def measure_hba1c(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "measure hba1c",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "measure hba1c", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "value": {
            "value": "72",
            "unit": "mmol/mol",
            "system": "http://unitsofmeasure.org",
            "code": "mmol/mol",
        },
    }

    new_patient_record_entries = [encounter, measure_hba1c]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=10),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
        24: datetime.timedelta(days=1),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 2: medication change 1 
# If hba1c hasn't changed in 6 months, can't happen on the first appointment

def medication_change1(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "medication change 1",
        "start": patient_time,
    }

    entry = { # not the hba1c in this one
        "resource_type" : "MedicationRequest",
        "name": "double therapy", # add a sulfonylurea to metformin, e.g. glicazide
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "value": {
          #  "value": 60,
          #  "unit": "mg",
          #  "system": "http://unitsofmeasure.org",
          #  "code": "mg",
        },
    }

    new_patient_record_entries = [encounter, medication_change1]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 3: medication change 2
# If hba1c hasn't changed in 6 months and interaction 2 has occurred, can't happen on the first appointment

def medication_change2(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "medication change 2",
        "start": patient_time,
    }

    entry = { # not the hba1c in this one
        "resource_type" : "MedicationRequest",
        "name": "double therapy", # add a third medication to metformin and sulf., e.g. glicazide
        "start": encounter["start"] + datetime.timedelta(minutes=10),
        "value": {
          #  "value": 60,
          #  "unit": "mg",
          #  "system": "http://unitsofmeasure.org",
          #  "code": "mg",
        },
    }

    new_patient_record_entries = [encounter, medication_change2]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 4: exercise prescription

def medication_change2(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "exercise_prescription",
        "start": patient_time,
    }

    entry = { # not the hba1c in this one
        "resource_type" : "Service Request",
        "name": "exericise prescription", # update values of cost etc.
        "start": encounter["start"] + datetime.timedelta(minutes=10),
    }

    new_patient_record_entries = [encounter, medication_change2]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 6: prediabetes diagnosis
# Call if hba1c is between 42 and 48 mmol/mol

def prediabetes_diagnosis(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "prediabetes diagnosis",
        "start": patient_time,
    }

    condition = {
        "resource_type": "Condition",
        "name" : "prediabetes",
        "start": patient_time,
    }

    entry = { # not the hba1c in this one
        "resource_type" : "Service Request",
        "name": "exericise prescription", # update values of cost etc.
        "start": encounter["start"] + datetime.timedelta(minutes=10),
    }

    new_patient_record_entries = [encounter, prediabetes_diagnosis]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} #call control.py instead

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Diabetes interaction 7: type 2 diabetes diagnosis
# Call if hba1c is over 48 mmol/mol

def t2dm_diagnosis(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "t2dm diagnosis",
        "start": patient_time,
    }

    entry = { # should be hba1c in this one
        "resource_type" : "Service Request",
        "name": "t2dm diagnosis", # change the condition value, update values of cost etc.
        "start": encounter["start"] + datetime.timedelta(minutes=10),
    }

    new_patient_record_entries = [encounter, t2dm_diagnosis]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} #call control.py instead

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )


# Diabetes interaction 8: glucose management
# Ongoing management of glucose by a GP 

def glucose_management(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "t2dm diagnosis",
        "start": patient_time,
    }

    entry = { # should be hba1c in this one
        "resource_type" : "Service Request",
        "name": "glucose management", # change the condition value, update values of cost etc.
        "start": encounter["start"] + datetime.timedelta(minutes=10),
    }

    new_patient_record_entries = [encounter, glucose_management]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )
    
# Diabetes interaction 9: annual health check
# Has to be able to trigger foot care etc as well.  

def annual_health_check(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "annual_health_check",
        "start": patient_time,
    }

    entry = { # should be hba1c in this one
        "resource_type" : "Service Request",
        "name": "annual_health_check", # change the condition value, update values of cost etc.
        "start": encounter["start"] + datetime.timedelta(minutes=10),
    }

    new_patient_record_entries = [encounter, annual_health_check]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 10: hypertension management
# measure blood pressure 

def hypertension_management(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "annual_health_check",
        "start": patient_time,
    }

    entry = { # should be hba1c in this one
        "resource_type" : "Service Request",
        "name": "annual_health_check", # change the condition value, update values of cost etc.
        "start": encounter["start"] + datetime.timedelta(minutes=10),
    }

    new_patient_record_entries = [encounter, hypertension_management]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 11: complications identification and management 
# sending patients to foot care, mental health, maternity etc.

def complications_id_mant(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "complications id and management",
        "start": patient_time,
    }

    entry = { # should be foot health, mental health, maternity in this one
        "resource_type" : "Service Request",
        "name": "complications id and management", # change the condition value, update values of cost etc.
        "start": encounter["start"] + datetime.timedelta(minutes=10),
    }

    new_patient_record_entries = [encounter, complications_id_mant]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Diabetes interaction 12: glucose clinic 
# primary care glucose clinic rather than GP managing glucose in 8.

def glucose_clinic(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "glucose_clinic",
        "start": patient_time,
    }

    entry = { # should be foot health, mental health, maternity in this one
        "resource_type" : "Service Request",
        "name": "glucose_clinic", # change the condition value, update values of cost etc.
        "start": encounter["start"] + datetime.timedelta(minutes=10),
    }

    new_patient_record_entries = [encounter, glucose_clinic]

    next_environment_id_to_prob = {0: 0.5, 9: 0.3, 24: 0.2} 

    next_environment_id_to_time = {
        0: datetime.timedelta(days=30),  # TODO: from initial patient_time (not last)
        9: datetime.timedelta(days=20),
    }

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )