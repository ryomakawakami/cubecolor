import cv2
import numpy as np

def filterImage(image):
    #blurred = cv2.GaussianBlur(image, (7, 7), 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, th = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    canny = cv2.Canny(th, 59, 36)

    kernel = np.ones((5, 5))
    dilated = cv2.dilate(canny, kernel, iterations = 1)

    return dilated
