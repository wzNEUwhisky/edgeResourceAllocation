from graph import *
from requests import *
import numpy as np
from DQN import *
'''
@author ZiQi Wei
@date 2019.5.18
'''

#SDN controller class
class SDN_controller:

    #init method
    def __init__(self):
        self.graph = Graph()
        self.actionSpace = []
        self.RL = DQN(self.action_size, self.feature_size, output_graph=True)
        self.requests = []

        #get the action spaces
        for cl in self.graph.cloudlets:
            for operate in [0,1,2]:
                action = (cl, operate)
                self.actionSpace.append(action)
        self.action_size = len(self.actionSpace)

        #get the feature size
        self.feature_size = 5+self.graph.cloudlet_number*self.graph.web_function_number*2 #dimension number of the state
        '''
        这里说一下公式的来源：
        对于状态的维度来说，首先包含了request的维度：5
        其次包含了其中全部的cloudlet的状态：graph.cloutlet_number
        之后，每一个cloudlet包含了全部的该cloudlet的web_function的状态：graph.function_number
        每一个webfunction也包含了两个维度：当前vnf的资源之和，以及正在其中的request的所需资源之和
        
        '''



    #the method to get the nearest cloudlet
    def get_nearest_cl(self,request):

        #get the position of the request's neareset_AP
        x_request = request.nearest_AP.x
        y_request = request.nearest_AP.y

        #the possible max value of the distance is 2 times of edgeRange
        d = 2 * self.graph.edgeRange
        nearest_node = None

        for node in self.graph.APs:
            d_temp = node.x + node.y - x_request - y_request
            if d_temp < d:
                d = d_temp
                nearest_node = node

        return nearest_node

    #return if it is successful
    def getrequest(self,request,action):

        cl = action[0]
        operate = action[1]

        if(operate == 1):
            #create a new VNF
            cl.create_VNF_entity(request.web_function.VNF_calcap)
            cl.request_list.append(request)
        elif(operate == 2):
            #reuse the VNF which is existed
            cl.request_list.append(request)
        else:
            #when operate == 0, drop the request
            pass

    #the method to get observation
    def getObservation(self,request):
        #build the observation vector
        state = np.array([1,6+self.graph.cloudlet_number*(self.graph.web_function_number*2)],#this is the dimension of the state
                               dtype=np.float32)
        i = 0
        for i in range(self.graph.cloudlet_number):
            for web_function in self.graph.web_functions:
                state[0][i] = self.graph.cloudlets[i].get_cal_existed(web_function) #get the cal_exist for this webfunction
                i += 1 #point to next dimension
                state[0][i] = self.graph.cloudlets[i].get_cal_request(web_function) #get the cal_request for this webfunction
                i += 1 #point to next dimension

        state[0][i] = request.nearest_AP.x
        i+=1
        state[0][i] = request.nearest_AP.y
        i+=1
        state[0][i] = request.web_function.id
        i+=1
        state[0][i] = request.package_rate
        i+=1
        state[0][i] = request.slots_during
        i+=1
        state[0][i] = request.max_time

        return state

    #init all the requests
    def create_all_requests(self):
        for i in range(5000):
            vk = np.random.sample(self.graph.APs)  # the nearest ap node
            fk = np.random.sample(self.graph.web_functions)  # 1the random web_function it use
            yk = np.random.randint(self.graph.packetrate[0], self.graph.packetrate[1] + 1)  # the random package rate
            tk = np.random.randint(self.graph.requestslot[0],
                                   self.graph.requestslot[1] + 1)  # the random request slot
            dk = np.random.randint(1, 10000)  # set a random time link

            request = Request(vk, fk, yk, tk, dk)
            self.requests.append(request)


    #the step after one slot
    def step(self,i):

        observation = self.getObservation(self.requests[i])

        action = self.RL.choose_action(observation)

        observation_ = self.getNextObservation(action,self.requests[i],self.requests[i+1])

        reward = self.getReward(action,self.requests[i])

        self.RL.store_transition(observation, action, reward, observation_)

        return reward
    #get next observation
    def getNextObservation(self,action,request,request_next):

        self.getrequest(request,action)
        return self.getObservation(request_next)

    #the method for pass a slot
    def passSlot(self):
        for cl in self.graph.cloudlets:
            for request in cl.request_list:
                #deal with all the requests
                pass


    #get the reward of this request
    def getReward(self,action,request):
        pass








