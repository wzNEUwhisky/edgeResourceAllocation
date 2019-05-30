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

sdn = SDN_controller()






