import numpy as np
import matplotlib.pyplot as plt
from nodes import *
from SDN_controller import *
from requests import *

def run():

    slot = 0 #init slot
    controller = SDN_controller() #init SDN controller
    network_graph = controller.graph
    amount_request = network_graph.requests
    request_list = []

    while(True):
        for i in range(amount_request):
            vk = np.random.sample(network_graph.APs) #the nearest ap node
            fk = np.random.sample(network_graph.web_functions) #the random web_function it use
            yk = np.random.randint(network_graph.packetrate[0],network_graph.packetrate[1]+1) #the random package rate
            tk = np.random.randint(network_graph.requestslot[0],network_graph.requestslot[1]+1) #the random request slot
            dk = np.random.randint(1,10000) #set a random time link



if __name__ == '__main__':
    run()
