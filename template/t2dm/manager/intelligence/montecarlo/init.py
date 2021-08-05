import uuid
import math

def create_pathway_tree():
  "create an initial game state"
  return 

def init(context):
  players = "patients"
  board = [None,]*47
  game = {
    "agent_name": "pathway",
    "services": services,
    "winner": [],
    "behaviors": ["pathway.py"],
    "position": [5,5],
    "hidden": True,
    "agents": patients,
    "game_logic": {
      "game_name": "t2dm_pathway",
      "patients": "template/t2dm/patient_infos.json"
    }
  }

  agents = [{ 
    "agent_name": "player",
    "behaviors": ["montecarlo.py"], 
    "game_tree": "",
    "board": board, "turn": True, "agent_id": players[0],
    "game_logic": {"sig": True}
    }, {
    "agent_name": "player",
    "behaviors": ["montecarlo.py"], 
    "game_tree": "",    
    "board": board, "turn": False, "agent_id": players[1],
    "game_logic": {"sig": False}
    } ]

  environments = 47
  count = 47

  return [game] + agents

