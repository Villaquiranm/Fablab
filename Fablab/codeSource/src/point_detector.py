# -*- coding:utf-8 -*-

import cv2
import numpy as np

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
    
    def compute_point_coordinates(self,img):
        r=-1
        c=-1
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        #binary = self._auto_canny(blur)

    # find contours
        #(contours, _) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        (contours, _) = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # draw contours over original image
        cv2.drawContours(img, contours,0, (0, 0, 255), 5)

    # display original image with contours
        #cv2.namedWindow("output", cv2.WINDOW_NORMAL)
        cv2.imshow("output", img)        
        if cv2.waitKey(1):
            r=-1
            
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
    

    def _auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged
