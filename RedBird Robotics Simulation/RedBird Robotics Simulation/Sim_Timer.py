from threading import Thread
from time import sleep

class Sim_Timer(object):
    """description of class"""
    PAUSED = False

    def __init__(self):
        self.counter = 0
        
    def run(self):
        while not PAUSED:
            sleep(1)
            self.update_time()

    def update_time(self):
        self.counter = self.counter + 1

    def get_current_timer(self):
        return self.counter

    def stop(self):
        PAUSED = True

    def reset(self):
        self.counter = 0