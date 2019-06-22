import numpy as np
import matplotlib.pyplot as plt
from nodes import *
from SDN_controller import *
from requests import *
from DQN import *

def run():
    pass

    # slot = 0 #init slot
    controller = SDN_controller() #init SDN controller
    print("contoller build complete")
    RL = DQN(controller.action_size, controller.feature_size, output_graph=True)
    print("RL cpmpleted")
    network_graph = controller.graph
    amount_request = network_graph.requests
    request_list = []

    while(True):

        #get the observation
        #observation = controller.getObservation()

        reward_in_slot = 0

        #restore the reward in each slot
        rewards = []
        actions = []
        requests = []

        for i in range(amount_request):
            vk = np.random.sample(network_graph.APs) #the nearest ap node
            fk = np.random.sample(network_graph.web_functions) #the random web_function it use
            yk = np.random.randint(network_graph.packetrate[0],network_graph.packetrate[1]+1) #the random package rate
            tk = np.random.randint(network_graph.requestslot[0],network_graph.requestslot[1]+1) #the random request slot
            dk = np.random.randint(1,10000) #set a random time link

            request = Request(vk,fk,yk,tk,dk)
            requests.append(request)
            #get the observation
            observation = controller.getObservation(request)

            #get the action
            action = RL.choose_action(observation)
            actions.append(action)

        # get the next observation
        observation_, reward = controller.step(actions,requests)

        # restore the memory
        RL.store_transition(observation, action, reward, observation_)

        if (i % 200 == 0):
            RL.learn()

        observation = observation_

        reward_in_slot += reward

        rewards.append(reward_in_slot)






if __name__ == '__main__':
    run()

