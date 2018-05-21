# -*-coding:utf-8 -*
import time
import Adafruit_PCA9685 #import the adafruit module

class Servomoteur:

    def __init__(self, channel, rapport):
        """
            Créer une instance de Servomoteur
            On en aura trois dans notre cas
        """

        self.channel = channel                 # la broche de la carte utilisée : entre 0 et 15
        self.dc = rapport                      # le rapport cyclique du servo
        self.period = 20.0                     # en millisecondes

        freq = 1000.0 / self.period            # Hz (ici 50 Hz)
#        self.pwm = Adafruit_PCA9685.PCA9685()  #Initialiser le PCA9685 en utilisant l'adresse par défaut(0x40)

        # choix initial : on place le servo en position initiale ie 0° -->Toff= 205 (en resolution de bits)
#        self.pwm.set_pwm(channel, 0, rapport*4096)  #(channel,Ton,Toff): Ton = 0 tjrs et Toff = dutyCycle*4096
#        self.pwm.set_pwm_freq(freq)            #Régler la fréquence


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
            self.dc = (angle/180 + 1)*5               # rapport cyclique correspondant à angle
#            self.pwm.set_pwm(self.channel, 0, self.dc*4096)
            #time.sleep(1)                                   # attendre 1 seconde
