
'''
@author ZiQi Wei
@date 2019.5.18
'''

#request class
class Request:

    def __init__(self, Vk, Fk, Yk, Tk, Dk):
        self.nearest_AP = Vk #The nearest AP note from the wireless end
        self.web_function = Fk #The kind of VNF
        self.package_rate = Yk #The package rate of the request
        self.slots_during = Tk #The time during of the request
        self.max_time = Dk #Dk is the limited time delay from request start to request finish

        self.rest_packet = self.package_rate * self.slots_during #the rest of the packet which has not been deal with
        self.run_time = 0 #the time from request start until now



