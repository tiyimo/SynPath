# Intelligence feeding in patient updates from glucose.py, pregnancy.py and smoking.py
# Is it here that you say you want it to happen once a year?
def update_glucose(glucose_update_to_prob):
    probs = list(glucose_update_to_prob.values())
    return np.random.choice(environment, p=probs)

def update_pregnancy(pregnant_to_prob):
    probs = list(pregnant_to_prob.values())
    return np.random.choice(environment, probs)

def update_smoking(stop_smoking_to_prob):
    probs = list(stop_smoking_to_prob.values())
    return np.random.choice(environment, p=probs)
