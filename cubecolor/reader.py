import cv2
import numpy as np
from scipy.cluster.vq import kmeans, vq
import os
import sys

def empty(_):
    pass

def dist(pt1, pt2):
    dx = pt1[0] - pt2[0]
    dy = pt1[1] - pt2[1]
    return dx * dx + dy * dy

imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
inPath = os.path.join(imageDir, 'r3.jpg')

img = cv2.imread(inPath, -1)

#id = cv2.VideoCapture(0)

#cv2.namedWindow("Parameters")
#cv2.resizeWindow("Parameters", 300, 100)
#cv2.createTrackbar("Threshold1", "Parameters", 0, 255, empty)
#cv2.createTrackbar("Threshold2", "Parameters", 255, 255, empty)

while True:
    #_, img = vid.read()
    
    #threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    #threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    # Split image into RGB and apply HPF to each
    rgb_planes = cv2.split(img)
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

    # Detect all contours
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Filter out small and non-solid contours, and save as facelets
    facelets = []
    for contour in contours:
        area = cv2.contourArea(contour)
        hull = cv2.convexHull(contour)
        hull_area = cv2.contourArea(hull)
        solidity = float(area)/hull_area

        if area < 600 or area > 6500 or solidity < 0.9:
            continue

        (x,y),(MA,ma),angle = cv2.fitEllipse(contour)
        
        M = cv2.moments(contour)
        cx = (int) (M['m10'] / M['m00'])
        cy = (int) (M['m01'] / M['m00'])

        facelets.append([contour, area, angle, (cx, cy)])

    # Draw contours on image
    imCopy = img.copy()
    c = [facelet[0] for facelet in facelets]
    #cv2.drawContours(imCopy, c, -1, (255, 255, 255), 2)

    # Cluster based on angle (face that facelet is on)
    codebook, _ = kmeans([facelet[2] for facelet in facelets], 3)
    cluster_indices, _ = vq([facelet[2] for facelet in facelets], codebook)

    clusters = [[], [], []]
    i = 0
    for facelet in facelets:
        clusters[cluster_indices[i]].append(facelet)
        i += 1
    clusters = np.array(clusters)

    # Remove things with angle far from median
    for i in range(len(clusters)):
        cluster = clusters[i]
        if len(cluster) > 9:
            median = np.median([facelet[2] for facelet in cluster])
            clusters[i] = [facelet for facelet in cluster if abs(facelet[2] - median) < 10]

    # Figure out removing which object minimizes total distance from center, until there are 9 objects
    for cluster in clusters:
        while len(cluster) > 9:
            """
            minDistSum = 1000000000
            minIndex = 0
            for index in range(len(cluster)):
                lessOneX = np.vstack(cluster[i][3][0] for i in range(len(cluster)) if i != index)
                lessOneY = np.vstack(cluster[i][3][1] for i in range(len(cluster)) if i != index)
                avg = (np.sum(lessOneX) / (len(cluster) - 1), np.sum(lessOneY) / (len(cluster) - 1))

                sum = 0
                for i in range(len(cluster) - 1):
                    sum += dist((lessOneX[i], lessOneY[i]), avg)

                if sum < minDistSum:
                    minDistSum = sum
                    minIndex = index
            del(cluster[minIndex])
            """

            maxSolidity = 0
            minIndex = 0
            for index in range(len(cluster)):
                c = np.vstack(cluster[i][0] for i in range(len(cluster)) if i != index)

                area = cv2.contourArea(c)
                hull = cv2.convexHull(c)
                hull_area = cv2.contourArea(hull)
                solidity = float(area)/hull_area

                if area < maxSolidity:
                    maxSolidity = solidity
                    minIndex = index
            del(cluster[minIndex])
    # Display
    i = 0
    for cluster in clusters:
        for facelet in cluster:
            color = ()
            if i == 0:
                color = (255, 0, 0)
            elif i == 1:
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)

            cx, cy = facelet[3]

            cv2.putText(imCopy, str(int(facelet[2])), (cx - 13, cy + 10), cv2.FONT_HERSHEY_COMPLEX, 0.4, color)
        i += 1

    cv2.imshow('image', imCopy)
    cv2.imshow('result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey()
cv2.destroyAllWindows()
