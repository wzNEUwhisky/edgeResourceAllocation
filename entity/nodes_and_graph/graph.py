import numpy as np
from nodes import *
import math
'''
@author ZiQi Wei
@date 2019.5.18
'''

class Graph:

    def __init__(self, edgeRange=20, APs=100, cloudlets=20, calcap=(2000,4000),\
                 web_functions=20, webcap=(80,400), AP_delay=(0.002,0.005),\
                 requests=1000, packetrate=(20,80), delay=(0.2,1.2),\
                 requestslot=(1,5), operation_price=0.25, init_price=(20,50),\
                 packet_transmission_price=(0.002,0.005)):
        self.edgeRange = edgeRange
        self.AP_number = APs #The number of AP nodes
        self.cloudlet_number = cloudlets #The number of cloudlets
        self.calcap = calcap #The range of calculation capality of cloudlets
        self.web_function_number = web_functions #The number of web functions
        self.webcap = webcap #The web calculation cap
        self.AP_delay = AP_delay #The propagate delay between two AP nodes
        self.requests = requests #The number of requests
        self.packetrate = packetrate #The range of packetrate
        self.delay = delay #The range of max point to point delay for each request
        self.requestslot = requestslot #The range of slots number for each request
        self.operation_price = operation_price #The operation price of each unit of calculation
        self.init_price = init_price #The range of the price for creating VNF entities
        self.packet_transmission_price = packet_transmission_price #The range of the price for transmit one packet
        self.APs = [] #the set of all the nodes
        self.cloudlets = [] #the set of all the cloudlets
        self.web_functions = [] #the set of web functions

        #create random topology of networks
        for i in range(self.AP_number):
            x = np.random.randint(0,self.edgeRange)
            y = np.random.randint(0,self.edgeRange)
            connect_delay = np.random.uniform(self.AP_delay[0],self.AP_delay[1])
            new_AP = AP(i,connect_delay,x,y,None)

            #make sure there are no nodes in the same place
            flag = 1
            while(flag == 1):
                flag = 0
                for node in self.APs:
                    if node.x == new_AP.x and node.y == new_AP.y:
                        flag = 1
                if flag == 1:
                    x = np.random.randint(0, self.AP_number)
                    y = np.random.randint(0, self.AP_number)
                    connect_delay = np.random.uniform(self.AP_delay[0], self.AP_delay[1])
                    new_AP = AP(i, connect_delay, x, y, None)
                else:
                    self.APs.append(new_AP)

        #create cloudlets
        for i in range(self.cloudlet_number):
            temp_AP = self.APs[i]
            temp_calcap = np.random.randint(self.calcap[0],self.calcap[1]+1)
            new_cloudlet = CL(temp_AP.id, temp_AP.connectDelay, temp_AP.x, temp_AP.y,\
                              temp_AP.bw, temp_calcap)
            self.cloudlets.append(new_cloudlet)

        #create web functions
        for i in range(self.web_function_number):
            functionCost_per_speed = np.random.randint(math.ceil(self.webcap[0]/self.packetrate[1]),math.ceil(self.webcap[1]/self.packetrate[1]))
            '''
            这里解释一下0.5——5的来历：
            因为整个网络中网络功能的能力需求是40——400M
            而对于request来说，packetrate的取值范围是20——80
            所以最大的速率就是当packetrate为80的时候，要满足网络能力在40——400M的范围之内，所以单位速度计算能力的花费应该在0.5——5之间
            '''
            manage_speed = self.packetrate[1]
            new_web_function = WebFunction(i, functionCost_per_speed,manage_speed)
            self.web_functions.append(new_web_function)


if __name__ == "__main__":
    graph = Graph()
    for node in graph.APs:
        print(node.x, node.y)

