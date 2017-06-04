from Sim_Timer import Sim_Timer
from threading import Thread
from random import randint
from math import tan, pow, sqrt

class Ground_Robot_Interface(Thread, object):
    """description of class"""
    def __init__(self, x, y, ID, color):
        self.x = x
        self.y = y
        self.ID = ID
        self.color = color
        self.deltaX = randint(-33, 33) / 100
        self.deltay = sqrt(((pow(0.33, 2)) - (pow(self.deltaX, 2))))
        self.angle = tan((self.deltay / self.deltaX))
        self.thread_cancelled = False
        self.collision = False

    def get_coordinates(self):
        pass

    def get_angle(self):
        pass

    def run(self):
        pass

    def cancel(self):
        pass

    def update_movement(self):
        pass

    def check_collisions(self, ):
        pass