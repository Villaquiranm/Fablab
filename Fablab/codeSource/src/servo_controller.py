#-*- coding: utf-8 -*-
from kinematic import *
from control_servo import *

class Servo_Controller:
    # Constructor
    # channel : tableau de trois elements pour les broches de la board
    def __init__(self, channel, rapport):
        self._x = 0.0
        self._y = 0.0
        self._servo1 = Servomoteur(channel[0], rapport)
        self._servo2 = Servomoteur(channel[1], rapport)
        self._servo3 = Servomoteur(channel[2], rapport)
        self._cinematique = Kinematic(24,70,245,95)

    # le vecteur direction (x,y) est normalisé
    # la valeur de z doit être constante
    def moveTowardsDirection(self,x,y):
        global cinematique
        # calculer les angles correspondant
        self._x = x
        self._y = y
        angles = self._cinematique.inverse_kinematic(self._x, self._y,-319)   # a voir pour la valeur de z
        # Actualiser le rapport cyclique et set la position des différents servos
        print "a1: ",angles[1],"a2: ",angles[2],"a3: ",angles[3]
        self._servo1.set_servo_pulse(angles[1])
        self._servo2.set_servo_pulse(angles[2])
        self._servo3.set_servo_pulse(angles[3])
 
