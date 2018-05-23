# Servo2.py
# Two servo motors driven by PCA9685 chip
   
from servo_controller import *

def init():
    global controler
    controler = Servo_Controller([0,1,2],5)

print "Initializing"
init()
controler.moveTowardsDirection(-50,0)

