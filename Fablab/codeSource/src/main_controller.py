from image_controller import *
from servo_controller import *

import time

SLEEP_TIME = 2

# Class managing all the controller and containing the main loop
class Main_Controller:
    def __init__(self):
        self._servoController = Servo_Controller()
        self._imageController = Image_Controller()
        #x,y = self._imageController.get_point_coordinates()
        #print('x='+str(x)+',y='+str(y))

    def main_loop(self):
        while (True):
            # Get point coordinates
            x,y = self._imageController.get_point_coordinates()

            if x==-1:
                time.sleep(SLEEP_TIME)
                continue

            # Move motors
            x = x-0.5
            y = y-0.5
            r = sqrt(x*x+y*y)
            self._servoController.moveTowardDirection(x/r,y/r)
            
            # Wait a little to be sure the motors are at the right location
            time.sleep(SLEEP_TIME)

    def on_destroy(self):
        self._imageController.on_destroy()
