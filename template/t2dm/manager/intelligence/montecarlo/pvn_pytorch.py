#From an implementation of the training pipeline of AlphaZero for Gomoku
# @author: Junxiao Song, updated for SynPath by TM

# Packages (PyTorch and Numpy)
import torch
import torch.nn as nn                           # builds graphs
from torch.nn.modules import module             # tensors and automatic differentiation modules
import torch.optim as optim                     # implements optimisation algorithms
import torch.nn.functional as F                 # applies convolution (operation on  2 functions producing a third)
from torch.autograd import Variable             # automatic differentiation, powers neural network training
import numpy as np                              # the usual

# Set the learning rate
def set_learning_rate(optimizer, lr):
    """Sets the learning rate to the given value"""
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

# Class is a category of things, self is an instance of that class. _init_ initialises the attributes of the class.
# Write the policy value network module as a class
class Net(nn.Module):
    """policy-value network module"""
    def __init__(self, cost, carbon, glucose):
        super(Net, self).__init__()

        self.cost = cost                #Read in from simulation outputs
        self.carbon = carbon 
        self.glucose = glucose

        # common layers *Conv1d because it's time series not an image?
        # 3 in channels (cost, carbon, glucose) and how many out?
        self.conv1 = nn.Conv1d(3, 1, kernel_size=3, padding=1)
        self.conv2 = nn.Conv1d(3, 1, kernel_size=3, padding=1) # fix figures
        self.conv3 = nn.Conv1d(3, 1, kernel_size=3, padding=1) # fix figures

        # action policy layers
        self.act_conv1 = nn.Conv1d(3, 1, kernel_size=1)
        self.act_fc1 = nn.Linear(cost, carbon, glucose)

        # state value layers
        self.val_conv1 = nn.Conv1d(3,1, kernel_size=1)
        self.val_fc1 = nn.Linear(cost, carbon, glucose, 3)
        self.val_fc2 = nn.Linear(3,1)

    def forward(state_input):
        # common layers (relu outputs positive input, or zero)
        x = F.relu(self.conv1(state_input))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        # action policy layers
        x_act = F.relu(self.act_conv1(x))
        x_act = x_act.view(-1, cost, carbon, glucose) #view function reshapes the tensor (object describing multilinear relationship)
        x_act = F.log_softmin(self.act_fc1(x_act)) # returns a tensor -inf to 0
        # state value layers
        x_val = F.relu(self.val_conv1(x))
        x_val = x_val.view(-1, 2*self.board_width*self.board_height)
        x_val = F.relu(self.val_fc1(x_val))
        x_val = F.tanh(self.val_fc2(x_val))
        return x_act, x_val

# Write the policy value network itself as a class 
class PolicyValueNet():
 """policy-value network """
    def __init__(self, cost, carbon, glucose,
                 model_file=None, use_gpu=False):
        self.use_gpu = use_gpu
        self.cost = cost
        self.carbon = carbon
        self.glucose = glucose
        self.l2_const = 1e-4  # coef of l2 penalty  # update?
        # the policy value net module
        if self.use_gpu:
            self.policy_value_net = Net(cost, carbon, glucose).cuda()
        else:
            self.policy_value_net = Net(cost, carbon, glucose)
        self.optimizer = optim.Adam(self.policy_value_net.parameters(),
                                    weight_decay=self.l2_const)

        if model_file:
            net_params = torch.load(model_file)
            self.policy_value_net.load_state_dict(net_params)

# Define the policy value (edit??)
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

# Policy value function
 def policy_value_fn(self, environments): # update
        """
        input: board
        output: a list of (action, probability) tuples for each available
        action and the score of the board state
        """
        legal_positions = environments
        current_state = np.ascontiguousarray(board.current_state().reshape(
                -1, 4, self.cost, self.carbon, self.glucose))
        if self.use_gpu:
            log_act_probs, value = self.policy_value_net(
                    Variable(torch.from_numpy(current_state)).cuda().float())
            act_probs = np.exp(log_act_probs.data.cpu().numpy().flatten())
        else:
            log_act_probs, value = self.policy_value_net(
                    Variable(torch.from_numpy(current_state)).float())
            act_probs = np.exp(log_act_probs.data.numpy().flatten())
        act_probs = zip(legal_positions, act_probs[legal_positions])
        value = value.data[0][0]
        return act_probs, value

# Define the training step
def train_step(self, state_batch, mcts_probs, min_batch, lr):
        """perform a training step"""
        # wrap in Variable
        if self.use_gpu:
            state_batch = Variable(torch.FloatTensor(state_batch).cuda())
            mcts_probs = Variable(torch.FloatTensor(mcts_probs).cuda())
            min_batch = Variable(torch.FloatTensor(min_batch).cuda())
        else:
            state_batch = Variable(torch.FloatTensor(state_batch))
            mcts_probs = Variable(torch.FloatTensor(mcts_probs))
            min_batch = Variable(torch.FloatTensor(min_batch))

        # zero the parameter gradients
        self.optimizer.zero_grad()
        # set learning rate
        set_learning_rate(self.optimizer, lr)

        # forward
        log_act_probs, value = self.policy_value_net(state_batch)
        # define the loss = (z - v)^2 - pi^T * log(p) + c||theta||^2
        # Note: the L2 penalty is incorporated in optimizer
        value_loss = F.mse_loss(value.view(-1), min_batch)
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