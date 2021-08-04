#  Validate reasonable actions (move to environments, and get patient updates)

def behavior(state, manager):
  pathway = manager.globals()["pathway"] 
  # need the globals.json to be updated to reflect number of environments
  # going to call it "pathway"

  # Determine valid actions based on position
  # TBC whether to give all patients a follow-up destination (e.g GP) after update
  def check_environment(environment): # update this so that it checks the next environment is valid
    new_environment = [i for i in range(41)] in zip(pathway["environment_id", environment])
     
    valid_destination = new_environment<=40 
  
    return valid_destination
  # Return only valid environments based on position
  all_environments = manager.globals()["environments"]
  state["environments"] = [environment for environment in all_environments if check_environment(environment)]