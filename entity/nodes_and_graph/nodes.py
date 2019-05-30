

'''
@author ZiQi Wei
@date 2019.5.18
'''


# AP node class
class AP:

    def __init__(self, id, connectDelay, x, y, bw):
        self.id = id
        self.connectDelay = connectDelay  # connection delay
        self.x = x  # row coord
        self.y = y  # line coord
        self.bw = bw # bandwidth

    def execute_request(self):
        #push the request to SDN
        pass


# cloudlet node class
class CL(AP):

    def __init__(self, id, connectDelay, x, y, bw, calcap):
        AP.__init__(self, id, connectDelay, x, y, bw)
        self.calcap = calcap  # calculation capacity
        self.rest_calcap = calcap # the rest of calculation capacity, it will equals to calculation capacity when init
        self.VNF_list = []
        self.wait_list = []

    #the method of create the VNF entity
    def create_VNF_entity(self, webfunction):
        new_VNF = VNF(id, webfunction)
        self.VNF_list.append(VNF)
        self.rest_calcap -= new_VNF.calcap

    #the method of how VNF deal with the request
    def execute_request(self):
        pass #the method how the VNF deal with the entity have to be trained



#VNF class
class VNF:

    def __init__(self, cloudlet_id, webfunction):
        self.cloudlet_id = cloudlet_id #the owner of the VNF entity
        self.calcap = webfunction.VNF_calcap #the calculation capacity of the VNF entity
        self.webFunction = WebFunction #the VNF entity's web function
        self.rest_calcap = self.calcap #the rest capacity of the VNF, which is same as calcap when init

    #receive the request and excute it
    def execute_request(self, request):
        #judge if the request is suitable for the VNF entity
        if request.Fk != self.webFunction:
            raise Exception("the kind of request is not suitable for the VNF")
        #change the attributes of the VNF entity
        self.rest_calcap = self.rest_calcap - request.package_rate


#webFunction
class WebFunction:

    def __init__(self, id, functionCost_per_speed, manage_speed):
        self.id = id # The id number of the function
        self.functionCost_per_speed = functionCost_per_speed #the calculation resource for each speed unit
        self.manage_speed = manage_speed #the calculate rate for the function
        self.VNF_calcap = functionCost_per_speed * manage_speed # for each function, it will has the fixed calcalation capacity


