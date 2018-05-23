# -*-coding:utf-8 -*
import time
from smbus import SMBus
from PCA9685 import PWM

class Servomoteur:
    global fPWM 
    fPWM = 50
    global i2c_address
    i2c_address = 0x40 # (standard) adapt to your module
    channel = 0 # adapt to your wiring
    channel2 = 1
    channel3 = 2
    global a
    global b
    a = 8.5 # adapt to your servo
    b = 2  # adapt to your servo

    def __init__(self, channel, rapport):
        """
            Créer une instance de Servomoteur
            On en aura trois dans notre cas
        """

        self.channel = channel                 # la broche de la carte utilisée : entre 0 et 15
        self.dc = rapport                      # le rapport cyclique du servo
        self.setup()                           #Régler la fréquence

    def setup(self):
        i2c_address
        global pwm
        bus = SMBus(1) # Raspberry Pi revision 2
        pwm = PWM(bus, i2c_address)
        pwm.setFreq(fPWM)
        
    def setDirection(self,direction):
        duty = a / 180 * direction + b
        pwm.setDuty(self.channel, duty)
        print "direction =", direction, "-> duty =", duty

        
    def set_servo_pulse(self, angle):
        """
            1/Calcul du rapport cyclique correspondant à l'angle
            de rotation dont on veut que le servo positionne le bras
            2/Positionne le servo
        """

        # 0° --> rc = 5% --> Toff = 205
        # 90° --> rc = 7.5% --> Toff = 307
        # 180° --> rc = 10% --> Toff = 410
        if angle <= 180 :
            self.setDirection(angle)
        # attendre 1 seconde
