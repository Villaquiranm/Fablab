#-*- coding: utf-8 -*-

# Source : http://forums.trossenrobotics.com/tutorials/introduction-129/delta-robot-kinematics-3276/

import math
import numpy as np

# Trigonometric constants
sqrt3  = math.sqrt(3.0)
pi     = 3.141592653
sin120 = sqrt3 / 2.0
cos120 = -0.5
tan60  = sqrt3
sin30  = 0.5
tan30  = 1.0 / sqrt3

class Kinematic:
    """La classe pour effectuer les calculs d'asservissement du robot"""

    def __init__(self,e,f,re,rf):
        """
            constructeur pour init les paramètres du robot

            e  =  76     #platform equilateral triangle side
            f  =  567    #base equilateral triangle side
            re = 1244    #lower legs parallelogram length
            rf =  524    #upper legs length
        """
        self.e = e
        self.f = f
        self.rf = rf
        self.re = re

    def forward_kinematic(self, theta1,theta2,theta3):
        """
            Méthode pour calculer la position de la nacelle
            du robot en fonction des angles des bras
        """
        x0 = 0.0
        y0 = 0.0
        z0 = 0.0

        t = (self.f-self.e) * tan30 / 2.0
        #conversion des angles en radian
        theta1 = np.deg2rad(theta1)
        theta2 = np.deg2rad(theta2)
        theta3 = np.deg2rad(theta3)

        #Coordonnées des points de jointures entre bras et barres parallèles
        #après translations de sorte à ce que les 3 sphères s'intersectent en E

        #J1'
        y1 = -(t + self.rf*math.cos(theta1) )
        z1 = -self.rf * math.sin(theta1)
        #J2'
        y2 = (t + self.rf*math.cos(theta2)) * sin30
        x2 = y2 * tan60  #sin30*tan60 = cos30
        z2 = -self.rf * math.sin(theta2)

        #J3'
        y3 = (t + self.rf*math.cos(theta3)) * sin30
        x3 = -y3 * tan60
        z3 = -self.rf * math.sin(theta3)

        #d
        dnm = (y2-y1)*x3 - (y3-y1)*x2
        #wi
        w1 = y1*y1 + z1*z1
        w2 = x2*x2 + y2*y2 + z2*z2
        w3 = x3*x3 + y3*y3 + z3*z3
        # x = (a1*z + b1)/dnm
        a1 = (z2-z1)*(y3-y1) - (z3-z1)*(y2-y1)
        b1= -( (w2-w1)*(y3-y1) - (w3-w1)*(y2-y1) ) / 2.0


        # y = (a2*z + b2)/dnm
        a2 = -(z2-z1)*x3 + (z3-z1)*x2
        b2 = ( (w2-w1)*x3 - (w3-w1)*x2) / 2.0

        # a*z^2 + b*z + c = 0
        a = a1**2 + a2**2 + dnm**2
        b = 2.0 * (a1*b1 + a2*(b2 - y1*dnm) - z1*(dnm**2))
        c = (b2 - y1*dnm)*(b2 - y1*dnm) + b1**2 + (dnm**2)*(z1**2 - self.re**2)

        # discriminant
        d = b*b - 4.0*a*c
        if d < 0.0:
            return [1,0,0,0] # discriminant negatif: return error,x,y,z

        #Les solutions du probleme
        #   d >= 0
        z0 = -0.5*(b + math.sqrt(d)) / a
        x0 = (a1*z0 + b1) / dnm
        y0 = (a2*z0 + b2) / dnm

        return [0,x0,y0,z0]

    def angle_YZ(self, x,y,z, theta = None):
        """
            Methode intermédiaire de calcul de l'angle de rotation
            dans le plan YZ
        """
        y1 = -0.5*0.57735*self.f # f/2 * tg 30 : F1
        y -= 0.5*0.57735*self.e # translation du centre sur le coté : E1
        # z = a + b*y
        a = (x**2 + y**2 + z**2 + self.rf**2 - self.re**2 - y1**2) / (2.0*z)
        b = (y1-y) / z

        # discriminant
        d = -(a + b*y1)*(a + b*y1) + self.rf*(b*b*self.rf + self.rf)
        if d<0:
            return [1,0] # discriminant negatif return error, theta

        yj = (y1 - a*b - math.sqrt(d)) / (b*b + 1) # choosing outer point
        zj = a + b*yj
        theta = math.atan(-zj / (y1-yj)) * 180.0 / pi + (180.0 if yj>y1 else 0.0)

        return [0,theta] # return error, theta

    def inverse_kinematic(self,x,y,z):
        """
            Méthode de calcul des angles de rotation des bras
            du robot en fonction de la position de la nacelle
            Utilise la methode angle_YZ !
        """
        theta1 = 0
        theta2 = 0
        theta3 = 0
        status = self.angle_YZ(x,y,z)

        if status[0] == 0:
            theta1 = status[1]
            status = self.angle_YZ(x*cos120 + y*sin120, y*cos120-x*sin120, z, theta2) # XY plane
        if status[0] == 0:
            theta2 = status[1]
            status = self.angle_YZ(x*cos120 - y*sin120, y*cos120 + x*sin120, z, theta3) # XZ plane
        theta3 = status[1]

        return [status[0],theta1,theta2,theta3]


