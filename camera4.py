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
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(3,3),0)
    laplacian = cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=5)
    cv2.imshow('blur',laplacian)
    ##gray = cv2.GaussianBlur(gray, (3, 3), 0)
    edgesImage = cv2.Canny(gray,33,100)
    #ret,edgesImage = cv2.threshold(gray,127,255,0)
    #edgesImage = auto_canny(gray)
    # Display the resulting frame
    contours, hierarchy = cv2.findContours(edgesImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    rect = max_area(contours)
    if rect is not None :
                x,y,w,h = rect
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #im2, contours, hierarchy = cv2.findContours(edgesImage,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('frame',frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
