from graph import *
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

        #get the action spaces
        for cl in self.graph.cloudlets:
            for operate in [0,1,2]:
                action = (cl, operate)
                self.actionSpace.append(action)
        self.action_size = len(self.actionSpace)

        #get the feature size
        self.feature_size = 5+graph.cloudlet_number*graph.web_function_number*2 #dimension number of the state
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


sdn = SDN_controller()






