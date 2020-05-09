import cv2
import numpy as np
import os.path
from get_contours import getContours
from filter_image import filterImage

def empty(_):
    pass

# Set directories
imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
inPath = os.path.join(imageDir, '1.jpg')
outPath = os.path.join(imageDir, 'output.jpg')

# Create trackers
#cv2.namedWindow("Parameters")
#cv2.resizeWindow("Parameters", 300, 100)
#cv2.createTrackbar("Threshold1", "Parameters", 59, 255, empty)
#cv2.createTrackbar("Threshold2", "Parameters", 36, 255, empty)

image = cv2.imread(inPath)

#vid = cv2.VideoCapture(0)

while True:
    #_, image = vid.read()
    imContour = image.copy()

    filtered = filterImage(image)

    getContours(filtered, imContour)

    cv2.imshow("Image", imContour)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
