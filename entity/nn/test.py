import numpy as np
import matplotlib.pyplot as plt
from nodes import *
from SDN_controller import *
from requests import *
from DQN import *

def run(n):
    pass

    # slot = 0 #init slot
    controller = SDN_controller() #init SDN controller
    controller.create_all_requests()
    rewards = []
    i = 0
    count = 1

    while(True):
        reward = controller.step(i)
        rewards.append(reward)
        i += 1
        if i%1000 == 0:
            controller.passSlot()
        i = i%5000
        count += 1

        if count == n:
            break

    x = [i for i in range(n)]
    y = rewards

    plt.plot(x,y)
    plt.xlabel("time")
    plt.ylabel("reward")
    plt.savefig("logs/result.png")
    plt.show()



if __name__ == '__main__':
    run(50000)

