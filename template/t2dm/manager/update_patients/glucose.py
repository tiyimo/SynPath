# Paranjape's model for simulating movement of glucose levels in patients.
# Wu's model of diabetes type 2 glucose cycles: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC546416/#S1

import scipy

def glucose_update(patient, patient_time):
 
   entry = {
        "resource_type": "Condition",
        "name": "glucose",
        "start": "patient_time",
   } 
        
    glucose_model = scipy.optimize.minimize() ## TBC 
        
    new_patient_record_entries = [entry, glucose_update]

    glucose_update_to_prob = {0: 0.95, 1: 0.05}

    update_data = {"new_patient_record_entries": new_patient_record_entries}
    return (
        patient,
        update_data,
        glucose_update_to_prob
    )