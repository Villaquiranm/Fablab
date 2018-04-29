from point_detector import *
import cv2

# Class that handles everything related to OpenCV and the camera
class Image_Controller:
    # Constructor
    def __init__(self):
        self._detector = Point_Detector()
        # Camera initialization
        self._cap = cv2.VideoCapture(0)

    # Returns the coordinates of the point seen by the camera
    def get_point_coordinates(self):
        ret, frame = self._cap.read()
        return self._detector.compute_point_coordinates(frame)

    # Method called when this controller is destroyed
    def on_destroy(self):
        self._cap.release()
