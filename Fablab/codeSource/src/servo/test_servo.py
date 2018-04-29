# -*-coding:utf-8 -*

from kinematic import *
from control_servo import *

servo1 = Servomoteur(0,205)    # broche 15 initialement à 0°
#servo2 = Servomoteur(13,205)    # broche 13 initialement à 0°
#servo3 = Servomoteur(11,205)    # broche 11 initialement à 0°

cinematique = Kinematic(50,100,200,200)
angle1 = cinematique.inverse_kinematic(0,0,-900)
angle2 = cinematique.inverse_kinematic(-10, 5, -500)

while(True):
    #servo3.set_servo_pulse(angle1[3])
    #servo2.set_servo_pulse(angle1[2])
    servo1.set_servo_pulse(angle1[1])
    #time.sleep(1)
    #servo3.set_servo_pulse(angle2[3])
    #servo2.set_servo_pulse(angle2[2])
    servo1.set_servo_pulse(angle2[1])
    #time.sleep(1)
