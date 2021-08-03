# Import all the packages (PyTorch - machine learning framework, https://pytorch.org/)
import datetime
import torch
import torch.nn as nn
from torch.nn.modules import module
import torch.optim as optim
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np

####### ADDED TBC
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

####### ADDED TBC
# Set the learning rate (what about epsilon decay (0.3 or another value?))
def set_learning_rate(optimizer, lr):
    """ Sets the learning rate to the given value"""
    for param_group in optimizer.param.groups:
        param_group['lr'] = lr

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

# Selecting the next environment
def get_next_environment_id(next_environment_id_to_prob):
    probs = list(next_environment_id_to_prob.values())
    environments = list(next_environment_id_to_prob)
    return np.random.choice(environments, p=probs)

# Selecting the next interaction
def select_interaction(patient, environment, patient_time, interaction_mapper):
    for i in range(15):
        interaction_name = np.random.choice(environment.interactions)
        if interaction_name == "death":
            continue
    return interaction_name, interaction_mapper[interaction_name]

# Check capacity
next_environment = next_environment_to_prob.keys()
time_to_next = next_environment_id_to_time.values()

environment_status = patients.count(time_to_next, next_environment) # patient_time rather than time_to_next?

def check_capacity(patient, environment, patient_time):
     if environment_status > environment_capacity:
         update next_environment_id_to_time = next_environment_id_to_time + datetime.timedelta(days=5)

# Run the interaction mapper
def intelligence(patient, environment, patient_time, interaction_mapper):

    interaction_name, interaction = select_interaction(
        patient, environment, patient_time, interaction_mapper
    )
    print(
        f"{datetime.datetime.now()} - Inside intelligence layer:\n"
        f"patient_name: {patient.name}\n"
        f"patient_time: {patient_time}\n"
        f"environment_name: {environment.name}\n"
        f"interaction_name: {interaction_name}\n"
    )

    (
        patient,
        environment,
        update_data,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    ) = interaction(patient, environment, patient_time)

    if len(next_environment_id_to_prob) > 0: # edit
        next_environment_id = get_next_environment_id(
            next_environment_id_to_prob
        )
    else:
        next_environment_id = None

    if len(next_environment_id_to_prob) > 0:
        patient_time = (
            patient_time + next_environment_id_to_time[next_environment_id]
        )

    interaction_names = [interaction_name]
    return (
        patient,
        environment,
        patient_time,
        update_data,
        next_environment_id,
        interaction_names,
        next_environment_id_to_prob,
        next_environment_id_to_time,
    )

# Create the neural net
class Net(nn.Module):
    """policy-value network module"""
    def __init__(self, environments): ##### to change to valid envs instead of board for SynPath
        super(Net, self).__init__()
        
        # common layers

        # action policy layers

        # state value layers
    def forward(self, state_input):
        # common layers

        # action policy layers

        # state value layers
        return # TBC

# PolicyValueNet - minimise glucose, carbon, cost
class PolicyValueNet():
    """policy-value network"""
    def __init__(self, board_width, board_height, model_file=None, use_gpu=False):
        self.use_gpu = use_gpu
        self.board_width = board_width ##### edit to reflect that it's a pathway with no locations
        self.board_height = board_height
        self.l2_const = 1e-4  # coef of l2 penalty
        # policy value net module
        if self.use_gpu:
            self.policy_value_net = Net(# pathway).cuda()
        else:
            self.policy_value_net = Net(# pathway)
        self.optimizer = optim.Adam(self.policy_value_net.parameters(),
                                    weight_decay=self.l2_const)

        if model_file:
            net_params = torch.load(model_file)
            self.policy_value_net.load_state_dict(net_params)
            def policy_value(self, state_batch):
        """
        input: a batch of states
        output: a batch of action probabilities and state values
        """
        if self.use_gpu:
            state_batch = Variable(torch.FloatTensor(state_batch).cuda())
            log_act_probs, value = self.policy_value_net(state_batch)
            act_probs = np.exp(log_act_probs.data.cpu().numpy())
            return act_probs, value.data.cpu().numpy()
        else:
            state_batch = Variable(torch.FloatTensor(state_batch))
            log_act_probs, value = self.policy_value_net(state_batch)
            act_probs = np.exp(log_act_probs.data.numpy())
            return act_probs, value.data.numpy()

    def policy_value_fn(self, board):
        """
        input: board
        output: a list of (action, probability) tuples for each available
        action and the score of the board state
        """
        legal_positions = # valid_environments
        current_state = np.ascontiguousarray(#pathway.current_state().reshape(
                -1, 4, self.board_width, self.board_height)) # edit to reflect that it's a pathway
        if self.use_gpu:
            log_act_probs, value = self.policy_value_net(
                    Variable(torch.from_numpy(current_state)).cuda().float())
            act_probs = np.exp(log_act_probs.data.cpu().numpy().flatten())
        else:
            log_act_probs, value = self.policy_value_net(
                    Variable(torch.from_numpy(current_state)).float())
            act_probs = np.exp(log_act_probs.data.numpy().flatten())
        act_probs = zip(legal_positions, act_probs[#valid environments])
        value = value.data[0][0]
        return act_probs, value

    def train_step(self, state_batch, mcts_probs, winner_batch, lr):
        """perform a training step"""
        # wrap in Variable
        if self.use_gpu:
            state_batch = Variable(torch.FloatTensor(state_batch).cuda())
            mcts_probs = Variable(torch.FloatTensor(mcts_probs).cuda())
            winner_batch = Variable(torch.FloatTensor(winner_batch).cuda())
        else:
            state_batch = Variable(torch.FloatTensor(state_batch))
            mcts_probs = Variable(torch.FloatTensor(mcts_probs))
            winner_batch = Variable(torch.FloatTensor(winner_batch))

        # zero the parameter gradients
        self.optimizer.zero_grad()
        # set learning rate
        set_learning_rate(self.optimizer, lr)

        # forward
        log_act_probs, value = self.policy_value_net(state_batch)
        # define the loss = (z - v)^2 - pi^T * log(p) + c||theta||^2
        # Note: the L2 penalty is incorporated in optimizer
        value_loss = F.mse_loss(value.view(-1), winner_batch)
        policy_loss = -torch.mean(torch.sum(mcts_probs*log_act_probs, 1))
        loss = value_loss + policy_loss
        # backward and optimize
        loss.backward()
        self.optimizer.step()
        # calc policy entropy, for monitoring only
        entropy = -torch.mean(
                torch.sum(torch.exp(log_act_probs) * log_act_probs, 1)
                )
        return loss.data[0], entropy.data[0]
        #for pytorch version >= 0.5 please use the following line instead.
        #return loss.item(), entropy.item()

    def get_policy_param(self):
        net_params = self.policy_value_net.state_dict()
        return net_params

    def save_model(self, model_file):
        """ save model params to file """
        net_params = self.get_policy_param()  # get model params
        torch.save(net_params, model_file)




