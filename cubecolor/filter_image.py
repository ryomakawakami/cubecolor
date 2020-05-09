import cv2
import numpy as np

def filterImage(image):
    blurred = cv2.GaussianBlur(image, (7, 7), 1)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    canny = cv2.Canny(th, threshold1, threshold2)

    kernel = np.ones((5, 5))
    dilated = cv2.dilate(canny, kernel, iterations = 1)

    return dilated
