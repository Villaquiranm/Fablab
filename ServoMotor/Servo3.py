# Servo2.py
# Two servo motors driven by PCA9685 chip

from smbus import SMBus
from PCA9685 import PWM
from kinematic import *
import time

fPWM = 50
i2c_address = 0x40 # (standard) adapt to your module
channel = 0 # adapt to your wiring
channel2 = 1
channel3 = 2
a = 8.5 # adapt to your servo
b = 2  # adapt to your servo

def setup():
    global pwm
    global cinematique
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)
    cinematique = Kinematic(50,100,200,200)

def setDirection(channel,direction):
    duty = a / 180 * direction + b
    pwm.setDuty(channel, duty)
    print "direction =", direction, "-> duty =", duty
    time.sleep(1) # allow to settle
   
print "starting"
setup()
angle = cinematique.inverse_kinematic(0, 0, -1)
setDirection(0,angle[0])
setDirection(1,angle[1])
setDirection(2,angle[2])
#x = cinematique.forward_kinematic(30,30,30)
#print "x:",x[1]," y:",x[2],"z: ",x[3]
    
    
print "done"
  

