#-*- coding: utf-8 -*-

# Source : http://forums.trossenrobotics.com/tutorials/introduction-129/delta-robot-kinematics-3276/

import math

# Specific geometry for the delta:
# Utiliser les dimensions de la structure du robot
#       en mm

# Micro-DELTA
# 115 457 232 112
# ABB flexpicker irb:  567 76 524 1244
e  =  76     #platform equilateral triangle side
f  =  567    #base equilateral triangle side
re = 1244    #lower legs parallelogram length
rf =  524    #upper legs length

# Trigonometric constants
sqrt3  = math.sqrt(3.0)
pi     = 3.141592653
sin120 = sqrt3 / 2.0
cos120 = -0.5
tan60  = sqrt3
sin30  = 0.5
tan30  = 1.0 / sqrt3

# Forward kinematics: (theta1, theta2, theta3) -> (x0, y0, z0)
# Position des 3 bras  ---->  Position de la nacelle
#   Return {error code,theta1,theta2,theta3}
#       0 si OK, 1 sinon
def forward(theta1, theta2, theta3):
    x0 = 0.0
    y0 = 0.0
    z0 = 0.0

    t = (f-e) * tan30 / 2.0
    dtr = pi / 180.0

    #conversion des angles en radian
    theta1 *= dtr
    theta2 *= dtr
    theta3 *= dtr

    #Coordonnées des points de jointures entre bras et barres parallèles
    #après translations de sorte à ce que les 3 sphères s'intersectent en E

    #J1'
    y1 = -(t + rf*math.cos(theta1) )
    z1 = -rf * math.sin(theta1)

    #J2'
    y2 = (t + rf*math.cos(theta2)) * sin30
    x2 = y2 * tan60  #sin30*tan60 = cos30
    z2 = -rf * math.sin(theta2)

    #J3'
    y3 = (t + rf*math.cos(theta3)) * sin30
    x3 = -y3 * tan60
    z3 = -rf * math.sin(theta3)

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
    a = a1*a1 + a2*a2 + dnm*dnm
    b = 2.0 * (a1*b1 + a2*(b2 - y1*dnm) - z1*dnm*dnm)
    c = (b2 - y1*dnm)*(b2 - y1*dnm) + b1*b1 + dnm*dnm*(z1*z1 - re*re)

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

# Inverse kinematics : (x0,y0,z0)  --->  (theta1, theta2, theta3)
# Position de la nacelle E0 ---> Angle de rotation des 3 bras
#       return 0,theta si Ok sinon 1,0
#calcul intermédiaire
def angle_yz(x0, y0, z0, theta=None):
    y1 = -0.5*0.57735*f # f/2 * tg 30 : F1
    y0 -= 0.5*0.57735*e # translation du centre sur le coté : E1
    # z = a + b*y
    a = (x0*x0 + y0*y0 + z0*z0 + rf*rf - re*re - y1*y1) / (2.0*z0)
    b = (y1-y0) / z0

    # discriminant
    d = -(a + b*y1)*(a + b*y1) + rf*(b*b*rf + rf)
    if d<0:
        return [1,0] # discriminant negatif return error, theta

    yj = (y1 - a*b - math.sqrt(d)) / (b*b + 1) # choosing outer point
    zj = a + b*yj
    theta = math.atan(-zj / (y1-yj)) * 180.0 / pi + (180.0 if yj>y1 else 0.0)

    return [0,theta] # return error, theta

def inverse(x0, y0, z0):
    theta1 = 0
    theta2 = 0
    theta3 = 0
    status = angle_yz(x0,y0,z0)

    if status[0] == 0:
        theta1 = status[1]
        status = angle_yz(x0*cos120 + y0*sin120, y0*cos120-x0*sin120, z0, theta2)
    if status[0] == 0:
        theta2 = status[1]
        status = angle_yz(x0*cos120 - y0*sin120, y0*cos120 + x0*sin120, z0, theta3)
    theta3 = status[1]

    return [status[0],theta1,theta2,theta3]


#cas de tests particuliers intéressants
# 1) tous les angles sont pareils --> X = Y = 0 et Z quelconque
# 2) la nacelle est à la position (0,0,z0) alignement avec le centre de la base--> theta1 = theta2 = theta3 = 0

#Exemples doc P.16
#   Les angles de rotation pour [0 0 -900]:
#       [-18.684175387173177, -18.684175387173177, -18.684175387173177]
#   Les angles de rotation pour [300 500 -1100]:
#       [49.45704491245842, -11.28863388647025, 22.779302914690113]

#   La position de la nacelle pour [0 0 0]:
#       [0.0, 0.0, -1050.8696065680476]
#   La position de la nacelle pour [10 20 30]:
#       [104.0642218312551, -173.5757804742531, -1232.1551384002278]

tab1 = inverse(0.0,0.0,-900.0)
print("Les angles de rotation pour [0 0 -900]:")
print(tab1[1:])

tab2 = inverse(300.0,500.0,-1100.0)
print("Les angles de rotation pour [300 500 -1100]:")
print(tab2[1:])

tab3 = forward(0,0,0)
print("La position de la nacelle pour [0 0 0]:")
print(tab3[1:])

tab4 = forward(10,20,30)
print("La position de la nacelle pour [10 20 30]:")
print(tab4[1:])
