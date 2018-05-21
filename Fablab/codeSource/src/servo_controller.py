#-*- coding: utf-8 -*-
from kinematic import *
from control_servo import *

class Servo_Controller:
    cinematique = Kinematic(50,100,200,200)     # variable globale
    # Constructor
    # channel : tableau de trois elements pour les broches de la board
    def __init__(self, channel, rapport):
        self._x = 0.0
        self._y = 0.0
        self._servo1 = Servomoteur(channel[0], rapport)
        self._servo2 = Servomoteur(channel[1], rapport)
        self._servo3 = Servomoteur(channel[2], rapport)

    # le vecteur direction (x,y) est normalisé
    # la valeur de z doit être constante
    def moveTowardsDirection(self,x,y):
        # calculer les angles correspondant
        angles = cinematique.inverse_kinematic(self._x, self._y, -350)   # a voir pour la valeur de z
        # Actualiser le rapport cyclique et set la position des différents servos
        self._servo1.set_servo_pulse(angles[1])
        self._servo2.set_servo_pulse(angles[2])
        self._servo3.set_servo_pulse(angles[3])
 
