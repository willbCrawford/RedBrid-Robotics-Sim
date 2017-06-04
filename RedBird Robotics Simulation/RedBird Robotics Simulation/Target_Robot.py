from Ground_RobotInterface import Ground_Robot_Interface
from Sim_Timer import Sim_Timer

class Target_Robot(Ground_Robot_Interface, object):
    """description of class"""
    global XYID
    def __init__(self, x, y, id, color, timer):
        self.timer = timer = Sim_Timer() 

        return super().__init__(x, y, id, color)

    def update_movement(self):
        while not self.thread_cancelled:
            self.x = self.deltaX + self.x
            self.y = self.deltaY + self.y

            self.current_pos = (self.x, self.y , self.ID)
            XYID = [self.current_pos]

    def check_collisions(self):
        min_num = 0
        max_num = 10
        for min_num in range(len(XYID)):
            if not (self.ID == min_num[2]):
                dXX = self.x - min_num[0]
                dYY = self.y - min_num[1]

                dCC = sqrt((pow(dXX, 2) + pow(dYY, 2)))

                if dCC <= 2*radius :
                    self.button_pushed(XYID[min_num])

            min_num = min_num + 1

    def button_pushed(self, robot):
         robot = Target_Robot
         
         vector_i = self.x - robot.x
         vector_j = self.y - robot.y

         theta = tan(vector_j / vector_i)

         min_theta = self.theta - 70
         max_theta = self.theta + 70

         if(theta >= min_theta and theta <= max_theta):
             self.button_pushed = True

    def run(self):
        current_time = self.timer.get_current_timer()

        while not self.timer.PAUSED and current_time < 20:
            self.update_movement()

            self.check_collision()

            current_time -= self.timer.get_current_timer()

    def error(self, current_position, velocity_vector, angle):
        errorVX = self.deltaX - velocity_vector[0]
        errorVY = self.detlaY - velocity_vector[1]

        if(errorVX >= 0.01):
            self.deltaX = velocity_vector[0]
            if(errorVY >= 0.01):
                self.deltaY = velocity_vector[1]
                

    def confidenceInterval(self, XY):
        counter = 0
        sum = 0
        for robot in self.XYID:
            sumX = sumX + robot[0]
            sumY = sumY + robot[1]
            counter += 1

        meanX = sumX/counter
        meanY = sumY/counter