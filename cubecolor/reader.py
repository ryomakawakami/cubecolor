import cv2
import numpy as np
import os.path
from get_contours import getContours
from filter_image import filterImage
from get_colors import getColors

def empty(_):
    pass

# Set directories
imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
inPath = os.path.join(imageDir, 's3.jpg')
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

    facelets = getColors(masked, imCopy)
        
    cv2.imshow("Image", imContour)
    cv2.imshow("Masked", masked)
    cv2.imshow("Color", imCopy)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
