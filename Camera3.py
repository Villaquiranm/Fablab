import numpy as np
import cv2

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged
def max_area(contours):
        i=0
        area=0
        maxRect = None
        
        for c in contours:
                rect = cv2.boundingRect(c)
                x,y,w,h = rect
                currentArea = x+y+w+h
                if currentArea > area:
                        area = currentArea
                        maxRect = rect
        return maxRect

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not working")

while(True):
    ret,im = cap.read()
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    thresh = auto_canny(imgray)
    cv2.imshow('canny',thresh)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(im, contours,0, (0,255,0), 3)
    rect = max_area(contours)
    if rect is not None :
                x,y,w,h = rect
                cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Img',im)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
