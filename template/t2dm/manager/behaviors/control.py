# Hash - https://core.hash.ai/@hash/qrl/1.0.0

import numpy as np

def behaviour(state, context):
    g = context.globals 
    
      if state["steps"] % g["episode_length"] == 0 or state["done"]:
    """record the episode rewards"""

    # Reset agent
    for key, value in g["agent_reset"].items():
      state[key] = value

    # Store and reset episode data
    state["episode"] += 1
    state["final_episode_reward"] = state["episode_reward"]
    state["episode_reward"] = 0
    state["steps"] = 1

    # Adjust hyperparameters
    state["epsilon"] *= (1 - g["epsilon_decay"])
    state["learning_rate"] *= (1 - g["learning_rate_decay"])
  
  state["steps"] += 1