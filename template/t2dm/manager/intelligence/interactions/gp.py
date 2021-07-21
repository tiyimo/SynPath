import datetime

# All the interactions at the gp
# "blood_test",
# "medication_change",
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
        "name" : "measure_hba1c",
        "start": patient_time,
    }

    hba1c = {
        "resource_type" : "Observation",
        "name": "hba1c", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
        "value": {
            "value": "72",
            "unit": "mmol/mol",
            "system": "http://unitsofmeasure.org",
            "code": "mmol/mol",
        },
    }

    new_patient_record_entries = [encounter, hba1c]

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

# Diabetes interaction 2: medication change 

def medication_change1(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "medication_change1",
        "start": patient_time,
    }

    hba1c = {
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

def medication_change2(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "medication_change1",
        "start": patient_time,
    }

    hba1c = {
        "resource_type" : "MedicationRequest",
        "name": "double therapy", # add a third medecation to metformin and sulf., e.g. glicazide
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
