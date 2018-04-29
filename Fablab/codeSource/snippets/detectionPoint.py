import cv2
import numpy
import sys

# Script qui va chercher à détecter des formes dans une image passée
# en entrée. Copie l'image en traçant un rectangle autour des formes
# détectées.
# Prend en paramètre le nom de l'image en entrée et le nom du fichier copié créé

DIST=5

if len(sys.argv) < 3:
    print "Usage : "+sys.argv[0]+" fichierEntree fichierSortie"
    sys.exit(1)
FILENAME=sys.argv[1]

groups = []
# groups[i][0] : row_min
# groups[i][1] : row_max
# groups[i][2] : col_min
# groups[i][3] : col_max
# groups[i][4] : nbPoints

def addToGroup(row,col,group):
    if row<group[0]:
        group[0] = row
    if row>group[1]:
        group[1] = row
    if col<group[2]:
        group[2] = col
    if col>group[3]:
        group[3] = col
    group[4] += 1
#end addToGroup

def belongsToGroup(row,col,group):
    if row>=group[0]-DIST and row<=group[1]+DIST and col>=group[2]-DIST and col<=group[3]+DIST:
        return True
    return False
#end belongsToGroup

def processDot(row,col):
    global groups
    i = 0
    while i<len(groups):
        if belongsToGroup(row,col,groups[i]):
            addToGroup(row,col,groups[i])
            return
        #end if
        i += 1
    #end while

    #create a new group
    groups.append( [row,row,col,col,1] )
#end processDot

# "main" function
# load image
img = cv2.imread(FILENAME,cv2.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]
img = cv2.resize(img,(600,int(600.0*height/width)),interpolation=cv2.INTER_CUBIC)

# edge detection
edges = cv2.Canny(img,100,200)

# center computation
nbRows = img.shape[0]
nbCols = img.shape[1]

# find the groups of points
for row in range(0,nbRows):
    for col in range(0,nbCols):
        if edges[row,col] == 255:
            processDot(row,col)
        #end if
    #end for
#end for

# draw the center of each group
for g in groups:
    for i in range(g[0],g[1]):
        img[i,g[2]] = 255
        img[i,g[3]] = 255
    for i in range(g[2],g[3]):
        img[g[0],i] = 255
        img[g[1],i] = 255

# write image
cv2.imwrite(sys.argv[2],img)
#cv2.imwrite('edges.png',edges)
