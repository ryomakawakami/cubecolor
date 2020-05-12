import cv2
import numpy as np

def filterImage(image):
    # Split image into RGB and apply HPF to each
    rgb_planes = cv2.split(image)
    result_planes = []
    kernel = np.array([[0, -1/8, 0], [-1/8, 2, -1/8], [0, -1/8, 0]])
    for plane in rgb_planes:
        plane = cv2.filter2D(plane, -1, kernel)
        result_planes.append(plane)
    result = cv2.merge(result_planes)

    # Make grayscale
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    # Make dark grays black
    _, result = cv2.threshold(result, 50, 255, cv2.THRESH_TOZERO)

    # Truncation
    _, th = cv2.threshold(gray, 160, 255, cv2.THRESH_TRUNC)

    # Morphology transformation to remove some noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    morph = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)

    # Canny and dilation
    canny = cv2.Canny(morph, 59, 36)
    kernel = np.ones((3, 3))
    dilated = cv2.dilate(canny, kernel, iterations = 1)

    return dilated
