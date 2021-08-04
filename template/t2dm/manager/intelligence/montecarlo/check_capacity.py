# Check capacity
next_environment = next_environment_to_prob.keys()
time_to_next = next_environment_id_to_time.values()

environment_status = patients.count(time_to_next, next_environment) # patient_time rather than time_to_next?

def check_capacity(patient, environment, patient_time):
     if environment_status > environment_capacity:
         update next_environment_id_to_time = next_environment_id_to_time + datetime.timedelta(days=5)