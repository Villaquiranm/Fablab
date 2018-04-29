# -*- coding:utf-8 -*-

import cv2

# Class that analyzes images and finds the closest point to the center
# with the method "vec2 compute_point_coordinates(image)"
class Point_Detector:
    # max distance between two pixels to be considered as pixels of the same group
    _DIST = 5

    # groups of pixels : a group is a rectangle defined by
    #    row_min = group[0]
    #    row_max = group[1]
    #    column_min = group[2]
    #    column_max = group[3]
    #    number of points in the group = group[4]
    _groups = []

    # Constructor
    def __init__(self):
        return

    # Method that finds the point closest to the center in the image passed as a parameter
    # Parameter :
    #   image : picture object coming from a camera or a file
    # Returns
    #   a tuple (x,y) corresponding to the coordinates of the point found with 0<=x,y<=1
    #   or (-1,-1) if no points are found
    def compute_point_coordinates(self,image):
        self._groups = []

        nbRows = image.shape[0]
        nbCols = image.shape[1]
        ratio = float(nbCols)/float(nbRows)

        # First we resize the picture to make the detection simpler
        resizedImage = cv2.resize(image,(600,int(ratio*600.0)),interpolation=cv2.INTER_CUBIC)

        nbRows = resizedImage.shape[0]
        nbCols = resizedImage.shape[1]

        # Then we want a grey picture
        grayImage = cv2.cvtColor(resizedImage,cv2.COLOR_BGR2GRAY)

        # After that we compute edges
        edgesImage = cv2.Canny(grayImage,100,200)
        #cv2.imwrite('truc.png',edgesImage)

        # Now we try to find the groups of points
        for row in range(0,nbRows-1):
            for col in range(0,nbCols-1):
                if(edgesImage[row,col]==255):
                    self._processDot(row,col)

        # Finally we keep the group closest to the center
        r = -1
        c = -1
        center = (nbRows/2,nbCols/2)
        for g in self._groups:
            # compute the center
            row = (g[0]+g[1])/2
            col = (g[2]+g[3])/2

            # if (row,col) is closer to the center than (r,c)
            if self._distanceSquare((row,col),center)<self._distanceSquare((r,c),center) :
                r = row
                c = col

        if r==-1:
            return -1,-1

        return c/float(nbCols),r/float(nbRows)

    # tests if the pixel (row,col) belongs to 'group'
    def _belongsToGroup(self,row,col,group):
        if row>=group[0]-self._DIST and row<=group[1]+self._DIST and col>=group[2]-self._DIST and col<=group[3]+self._DIST:
            return True
        return False

    # Adds the pixel (row,col) to 'group'
    def _addToGroup(self,row,col,group):
        if row<group[0]:
            group[0] = row
        if row>group[1]:
            group[1] = row
        if col<group[2]:
            group[2] = col
        if col>group[3]:
            group[3] = col
        group[4] += 1

    # Looks for a group where to add the pixel (row,col)
    # Creates one if none is found
    def _processDot(self,row,col):      
        i = 0
        while i<len(self._groups):
            if self._belongsToGroup(row,col,self._groups[i]):
                self._addToGroup(row,col,self._groups[i])
                return
            i += 1

        #create a new group
        self._groups.append( [row,row,col,col,1] )

    # Computes the square distance between p1 and p2
    def _distanceSquare(self,p1,p2):
        return (p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1])
