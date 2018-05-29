# Servo2.py
# Two servo motors driven by PCA9685 chip
   
from servo_controller import *

def init():
    global controler
    controler = Servo_Controller([0,1,2],5)

print "Initializing"
init()
#for x in range(-70,70,10):
    #for y in range(0,50,1):
controler.moveTowardsDirection(0,0)
#    time.sleep(1)

