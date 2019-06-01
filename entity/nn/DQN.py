import numpy as np
import tensorflow as tf
import pandas as pd


class DQN:

    def __init__(self,n_actions,n_features,action_size=2, learning_rate=0.01,reward_decay=0.9,\
                 e_greedy=0.9,replace_target_iter=300,memory_size=500,\
                 batch_size=32,e_greedy_increment=None,output_graph=False):
        self.n_actions = n_actions
        self.n_features = n_features
        self.action_size = action_size #dimension for action: cl + [0(delete),1(create),2(reuse)]
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon_max = e_greedy
        self.replace_target_iter = replace_target_iter
        self.memory_size = memory_size
        self.batch_size = batch_size
        self.epsilon_increament = e_greedy_increment
        self.epsilon = 0 if e_greedy_increment is not None else self.epsilon_max

        #learning step
        self.learn_step_counter = 0

        #initialize zero memory
        self.memory = np.zeros

