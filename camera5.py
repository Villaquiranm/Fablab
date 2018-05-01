'''
 * Python program to use contours to count the objects in an image.
 *
 * usage: python Contours.py <filename> <threshold>
'''
import cv2, sys
import numpy as np

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("camera off")
while(True):
    ret,img = cap.read()

    # create binary image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    binary = auto_canny(blur)

# find contours
    (contours, _) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# print table of contours and sizes
    #print("Found %d objects." % len(contours))
    #for (i, c) in enumerate(contours):
     #   print("\tSize of contour %d: %d" % (i, len(c)))

# draw contours over original image
    cv2.drawContours(img, contours, -1, (0, 0, 255), 5)

# display original image with contours
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.imshow("output", img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
