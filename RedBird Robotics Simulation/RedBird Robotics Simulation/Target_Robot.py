from Ground_RobotInterface import Ground_Robot_Interface
from Sim_Timer import Sim_Timer

class Target_Robot(Ground_Robot_Interface, object):
    """description of class"""
    XYID = []
    def __init__(self, timer = Sim_Timer()):
        return super().__init__()
        self.timer = timer

    def update_movement(self):
        while not self.thread_cancelled:
            self.x += self.deltaX
            self.y += self.deltaY

            self.current_pos = (self.x, self.y , self.ID)
            XYID.append(self.current_pos)

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
        errorX = self.current_pos[0] - current_position[0]
        errorY = self.current_pos[1] - current_position[1]

        if errorX >= 0.01:
             
