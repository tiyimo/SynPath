import datetime

# Interaction for patient with learning disabilities
# "adj_to_care"

# Diabetes interaction 16: Adjustments to care
# This can mean adjusting lifestyle education so that it meets the needs of people with learning disabilities

def adj_to_care(patient, environment, patient_time):
    encounter = {
        "resource_type": "Encounter",
        "name" : "adjustments to care",
        "start": patient_time,
    }

    entry = {
        "resource_type" : "Observation",
        "name": "adjustments to care", 
        "start": encounter["start"] + datetime.timedelta(minutes=15),
    }

    new_patient_record_entries = [encounter, adj_to_care]

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
