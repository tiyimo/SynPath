#From an implementation of the training pipeline of AlphaZero for Gomoku
# @author: Junxiao Song, updated for SynPath by TM

from __future__ import print_function
import random
import numpy as np
from collections import defaultdict, deque                #??
from t2dm import environments, interactions               # import values from env as pathway
from patient_abm import Patient                           # ok
from pvn_pytorch import PolicyValueNet                    # Pytorch

class TrainPipeline():
    def __init__(self, init_model=None):
        # params of the pathway and the simulation
        self.cost = 47
        self.carbon = 47
        self.glucose = 47
        self.pathway = Pathway(cost=self.cost,
                             carbon=self.carbon,
                             glucose=self.glucose)
        self.interactions=Interaction(self.pathway)
        #training params #change these
        self.learn_rate = 2e-3 
        self.lr_multiplier = 1.0
        self.temp = 1.0  # the temperature param
        self.n_playout = 400  # num of simulations for each move
        self.c_puct = 5
        self.buffer_size = 10000
        self.batch_size = 512  # mini-batch size for training
        self.data_buffer = deque(maxlen=self.buffer_size)
        self.play_batch_size = 1
        self.epochs = 5  # num of train_steps for each update
        self.kl_targ = 0.02
        self.check_freq = 50
        self.game_batch_num = 1500
        self.best_win_ratio = 0.0
        # num of simulations used for the pure mcts, which is used as
        # the opponent to evaluate the trained policy
        self.pure_mcts_playout_num = 10000
        if init_model:
            # start training from an initial policy-value net
            self.policy_value_net = PolicyValueNet(self.cost,
                                                   self.carbon,
                                                   self.glucose,
                                                   model_file=init_model)
        else:
            # start training from a new policy-value net
            self.policy_value_net = PolicyValueNet(self.cost,
                                                   self.carbon, 
                                                   self.glucose)
        self.patient = Patient(self.policy_value_net.policy_value_fn,
                               c_puct=self.c_puct,
                               n_playout = self.n_playout, 
                               is_selfplay=1)

## Do we neet get_equi_date in here? and self-play data

def policy_update(self):
    """update the policy-value net"""
    mini_batch = random.sample(self.data_buffer, self.batch_size)
    state_batch = [data[0] for data in mini_batch]
    mcts_probs_batch = [data[1] for data in mini_batch]
    min_batch = [data[2] for data in mini_batch]
    old_probs, old_v = self.policy_value_net.policy_value(state_batch)
    for i in range(self.epochs):
        loss, entropy = self.policy_value_net.train_step(
            state_batch,
            mcts_probs_batch,
            min_batch,
            self.learn_rate*self.lr_multiplier)
        new_probs, new_v = self.policy_value_net.policy_value(state_batch)
        kl = np.mean(np.sum(old_probs * (
                np.log(old_probs + 1e-10) - np.log(new_probs + 1e-10)),
                axis=1)
        )
        if kl > self.kl_targ * 4: # early stopping if D_KL diverges badly
            break
    # adaptively adjust the learning rate
    if kl > self.kl_targ * 2 and self.lr_multiplier > 0.1:
        self.lr_multiplier /=1.5
    elif kl < self.kl_targ /2 and self.lr_multiplier < 10:
        self.lr_multiplier *= 1.5
    
    explained_var_old = (1 - 
                         np.var(np.array(min_batch) - old_v.flatten())/
                         np.var(np.array(min_batch)))
    explained_var_new = (1 - 
                         np.var(np.array(min_batch) - new_v.flatten())/
                         np.var(np.array(min_batch)))
    
    print(("kl:{:.5f},"
               "lr_multiplier:{:.3f},"
               "loss:{},"
               "entropy:{},"
               "explained_var_old:{:.3f},"
               "explained_var_new:{:.3f}"
               ).format(kl,
                        self.lr_multiplier,
                        loss,
                        entropy,
                        explained_var_old,
                        explained_var_new))
        return loss, entropy

# Add a pathway evaluation by 'playing against' pure mcts
def policy_evaluate(self, n_pathways=10):
        """
        Evaluate the trained policy by running pathways against the pure MCTS player
        Note: this is only for monitoring the progress of training
        """
        current_mcts_player = Patient(self.policy_value_net.policy_value_fn,
                                         c_puct=self.c_puct,
                                         n_playout=self.n_playout)
        pure_mcts_player = MCTS_Pure(c_puct=5,
                                     n_playout=self.pure_mcts_playout_num)
        win_cnt = defaultdict(int)
        for i in range(n_pathways):
            winner = self.game.start_play(current_mcts_player,
                                          pure_mcts_player,
                                          start_player=i % 2,
                                          is_shown=0)
            win_cnt[winner] += 1
        win_ratio = 1.0*(win_cnt[1] + 0.5*win_cnt[-1]) / n_pathways
        print("num_playouts:{}, win: {}, lose: {}, tie:{}".format(
                self.pure_mcts_playout_num,
                win_cnt[1], win_cnt[2], win_cnt[-1]))
        return win_ratio

# Run the training pipeline (edit because this currently plays against itself):

def run(self):
        """run the training pipeline"""
        try:
            for i in range(self.game_batch_num):
                self.collect_selfplay_data(self.play_batch_size)
                print("batch i:{}, episode_len:{}".format(
                        i+1, self.episode_len))
                if len(self.data_buffer) > self.batch_size:
                    loss, entropy = self.policy_update()
                # check the performance of the current model,
                # and save the model params
                if (i+1) % self.check_freq == 0:
                    print("current self-play batch: {}".format(i+1))
                    win_ratio = self.policy_evaluate()
                    self.policy_value_net.save_model('./current_policy.model')
                    if win_ratio > self.best_win_ratio:
                        print("New best policy!!!!!!!!")
                        self.best_win_ratio = win_ratio
                        # update the best_policy
                        self.policy_value_net.save_model('./best_policy.model')
                        if (self.best_win_ratio == 1.0 and
                                self.pure_mcts_playout_num < 5000):
                            self.pure_mcts_playout_num += 1000
                            self.best_win_ratio = 0.0
        except KeyboardInterrupt:
            print('\n\rquit')


if __name__ == '__main__':
    training_pipeline = TrainPipeline()
    training_pipeline.run()
