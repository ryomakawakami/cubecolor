import cv2
import numpy as np
import os.path
from get_contours import getContours
from filter_image import filterImage

def empty(_):
    pass

colors = ['r', 'o', 'y', 'g', 'b', 'w']

# Set directories
imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
inPath = os.path.join(imageDir, 's1.jpg')
outPath = os.path.join(imageDir, 'output.jpg')

# Create trackers
#cv2.namedWindow("Parameters")
#cv2.resizeWindow("Parameters", 300, 100)
#cv2.createTrackbar("Threshold1", "Parameters", 0, 255, empty)
#cv2.createTrackbar("Threshold2", "Parameters", 10, 255, empty)

image = cv2.imread(inPath)

#vid = cv2.VideoCapture(0)

while True:
    #_, image = vid.read()
    imContour = image.copy()
    imCopy = image.copy()

    filtered = filterImage(image)

    mask = getContours(filtered, imContour)
    masked = cv2.bitwise_and(image, image, mask=mask)
    masked_hsv = cv2.cvtColor(masked, cv2.COLOR_BGR2HSV)

    facelets = {}
    facelets['r'] = cv2.inRange(masked_hsv, (0, 100, 50), (10, 255, 255))    # Red
    facelets['o'] = cv2.inRange(masked_hsv, (10, 100, 50), (25, 255, 255))   # Orange
    facelets['y'] = cv2.inRange(masked_hsv, (27, 100, 50), (35, 255, 255))   # Yellow
    facelets['g'] = cv2.inRange(masked_hsv, (40, 100, 50), (80, 255, 255))   # Green
    facelets['b'] = cv2.inRange(masked_hsv, (80, 100, 50), (130, 255, 255))  # Blue
    facelets['w'] = cv2.inRange(masked_hsv, (0, 0, 100), (255, 20, 255))     # White

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    contours = []
    for color in colors:
        morph = cv2.morphologyEx(facelets[color], cv2.MORPH_OPEN, kernel)
        c, hierarchy = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        for x in c:
            area = cv2.contourArea(x)
            per = cv2.arcLength(x, True)
            if area > 800 and per < 1500:
                contours.append(x)

    cv2.drawContours(imCopy, contours, -1, (0, 0, 255), 3)

    cv2.imshow("Image", imContour)
    cv2.imshow("Masked", masked)
    cv2.imshow("Color", imCopy)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
