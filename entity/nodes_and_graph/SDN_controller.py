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

    #return if it is successful
    def getrequest(self,request,cl,action):
        if(action == 1):
            #create a new VNF
            if(cl.rest_calcap < request.web_function.VNF_calcap):
                #this means the rest calculation capacity can not offer a new VNF for this web function
                cl.wait_list.append(request)
            else:
                cl.create_VNF_entity(request.web_function.VNF_calcap)
        else:
            #reuse the VNF which is existed
            flag = False #judge if the vnf existed can be used
            for vnf in cl.VNF_list:
                if(vnf.webFunction.__eq__(request.web_function)):
                    if(vnf.rest_calcap > request.package_rate):
                        vnf.execute_request(request)
                        flag = True

            if(flag == False):
                #this means no vnf existed can be used
                cl.wait_list.append(request)


sdn = SDN_controller()






