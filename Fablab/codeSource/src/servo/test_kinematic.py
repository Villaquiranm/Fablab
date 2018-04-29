#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import numpy as np
from math import *
from kinematic import *

cinematique = Kinematic(50,100,200,200)

#Exemples doc P.16 et 19
#   Les angles de rotation pour [0 0 -900]:
#       [-18.684175387173177, -18.684175387173177, -18.684175387173177]
#   Les angles de rotation pour [300 500 -1100]:
#       [49.45704491245842, -11.28863388647025, 22.779302914690113]

#   La position de la nacelle pour [0 0 0]:
#       [0.0, 0.0, -1050.8696065680476]
#   La position de la nacelle pour [10 20 30]:
#       [104.0642218312551, -173.5757804742531, -1232.1551384002278]
#cinematique = Kinematic(76,567,1244,524)
#tab1 = cinematique.inverse_kinematic(0.0,0.0,-900.0)
#print("Les angles de rotation pour [0 0 -900]:")
#print(tab1[1:])

#tab2 = cinematique.inverse_kinematic(300.0,500.0,-1100.0)
#print("Les angles de rotation pour [300 500 -1100]:")
#print(tab2[1:])

#tab3 = cinematique.forward_kinematic(0,0,0)
#print("La position de la nacelle pour [0 0 0]:")
#print(tab3[1:])

#tab4 = cinematique.forward_kinematic(10,20,30)
#print("La position de la nacelle pour [10 20 30]:")
#print(tab4[1:])



# Translation selon l'axe z
for i in range(1,401):
    tab = cinematique.inverse_kinematic(0.0,0.0,-i)
    sortie = str(i) + " ; "
    sortie = sortie + str(tab[1]) + " ; " + str(tab[2]) + " ; " + str(tab[3])
    #print(sortie)

    # Remarque : un certain nombre de valeurs semble incohérent (jusqu'à 159).
    # En réalité ces valeurs (ormis le triplet de 0 qui correspond à une position impossible à atteindre pour le robot) correspondent à une remontée de la nacelle vers le haut en rentrant les articulations attachées à la nacelle vers l'intérieur du robot.

    # Pas de panique donc, tout s'explique !

print("\n\n")
    
# Translation selon l'axe x (symétrique étudié en même temps)
for i in range(1,200):
    tab = cinematique.inverse_kinematic(i,0.0,-100)
    tab2 = cinematique.inverse_kinematic(-i,0.0,-100)
    sortie = str(i) + " ; " + str(tab[1]) + " ; " + str(tab[2]) + " ; " + str(tab[3]) + "\n"
    sortie = sortie + str(-i) + " ; " + str(tab2[1]) + " ; " + str(tab2[2]) + " ; " + str(tab2[3])
    #print(sortie)

print("\n\n")

# Translation selon l'axe y (devrait se comporter comme celle selon x)
for i in range(1,200):
    tab = cinematique.inverse_kinematic(0,i,-100)
    tab2 = cinematique.inverse_kinematic(0,-i,-100)
    sortie = str(i) + " ; " + str(tab[1]) + " ; " + str(tab[2]) + " ; " + str(tab[3]) + "\n"
    sortie = sortie + str(-i) + " ; " + str(tab2[1]) + " ; " + str(tab2[2]) + " ; " + str(tab2[3])
    print(sortie)
