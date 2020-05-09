import cv2
import numpy as np
import os.path

def empty(_):
    pass

def getContours(img, out):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #facelets = []

    # Get the outline of the cube
    max = contours[0]
    maxArea = cv2.contourArea(max)
    for contour in contours:
        area = cv2.contourArea(contour)
        #if area > 1500 and area < 7000:
        #    facelets.append(contour)
        
        if area > maxArea:
            maxArea = area
            max = contour

    hull = max

    #cube = np.vstack(facelets[i] for i in range(len(facelets)))
    #hull = cv2.convexHull(cube)

    # Find the convex hull of the outline (hopefully 6 points)
    epsilon = 0.02 * cv2.arcLength(hull, True)
    poly = cv2.approxPolyDP(hull, epsilon, True)
    hull = cv2.convexHull(poly)

    cv2.drawContours(out, hull, -1, (0, 0, 255), 10)

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 300, 100)
cv2.createTrackbar("Threshold1", "Parameters", 59, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 36, 255, empty)

imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'images'))
inPath = os.path.join(imageDir, '1.jpg')
outPath = os.path.join(imageDir, 'output.jpg')

image = cv2.imread(inPath)

#vid = cv2.VideoCapture(0)

while True:
    #_, image = vid.read()
    imContour = image.copy()

    blurred = cv2.GaussianBlur(image, (7, 7), 1)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    _, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    canny = cv2.Canny(th, threshold1, threshold2)

    kernel = np.ones((5, 5))
    dilated = cv2.dilate(canny, kernel, iterations = 1)

    getContours(dilated, imContour)

    cv2.imshow("Image", imContour)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
