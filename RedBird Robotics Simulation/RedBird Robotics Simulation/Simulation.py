from Sim_Timer import Sim_Timer
from Target_Robot import Target_Robot
from math import pow, sqrt

class Simulation(object):
    """description of class"""
    def __init__(self):
        timer = Timing()

        robot = Target_Robot(timer)

        self.target_robot = []

        self.target_robot.append(robot)




