#!/usr/bin/python3.4
# -*-coding:utf-8 -*

import numpy as np
from math import *
from cinematique import *

# Translation selon l'axe z
for i in range(1,401):
    tab = inverse(0.0,0.0,-i)
    resultat = "Essai avec la position [0,0,-"
    resultat = resultat + str(i) + "] :"
    print(resultat)
    print(tab[1:])

    # Remarque : un certain nombre de valeurs semble incohérent (jusqu'à 159).
    # En réalité ces valeurs (ormis le triplet de 0 qui correspond à une position impossible à atteindre pour le robot) correspondent à une remontée de la nacelle vers le haut en rentrant les articulations attachées à la nacelle vers l'intérieur du robot.

    # Pas de panique donc, tout s'explique !

print("\n\n")
    
# Translation selon l'axe x (symétrique étudié en même temps)
for i in range(1,200):
    tab = inverse(i,0.0,-100)
    tab2 = inverse(-i,0.0,-100)
    resultat = "Essai avec la position ["
    resultat = resultat + str(i) + ",0,-100] :"
    print(resultat)
    print(tab[1:])
    print(tab2[1:])

print("\n\n")

# Translation selon l'axe y (devrait se comporter comme celle selon x)
for i in range(1,200):
    tab = inverse(0,i,-100)
    tab2 = inverse(0,-i,-100)
    resultat = "Essai avec la position [0,"
    resultat = resultat + str(i) + ",-100] :"
    print(resultat)
    print(tab[1:])
    print(tab2[1:])
