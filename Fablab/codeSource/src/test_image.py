from point_detector import *
import cv2

# Liste d'images avec
#    - le nom du fichier
#    - la position horizontale du point attendue
#    - la position verticale du point attendue
liste = [("pictures/test1.png",0.423,0.488),
        ("pictures/test2.png",0.475,0.362),
        ("pictures/test3.png",0.475,0.362),
        ("pictures/test4.png",-1,-1)]

# Fonction de comparaison des valeurs avec une certaine marge d'erreur autorisée
def test_values(result,expected):
    if abs(result-expected) > 0.05:
        print "Expected : "+str(expected)+", result : "+str(result)

# Initialisations
detector = Point_Detector()

# Execution des tests
for element in liste:
    print "Test "+element[0]

    # Analyse de l'image
    img = cv2.imread(element[0],cv2.IMREAD_COLOR)
    res = detector.compute_point_coordinates(img)

    # Comparaison des valeurs attendues et obtenues
    test_values(res[0],element[1])
    test_values(res[1],element[2])

print "Test fini"
