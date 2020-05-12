import cv2
import numpy as np
from scipy.cluster.vq import kmeans, vq
import os

def empty(_):
    pass

imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
inPath = os.path.join(imageDir, 'r2.jpg')

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

    # FIND QUADRILATERAL FIT FOR CLUSTERS
    #np.median([cluster[1] for cluster in clusters[0]])
    #clusters[0] = sorted(clusters[0], key=lambda a_entry: a_entry[1])
    #print([cluster[1] for cluster in clusters[0]])
    #while len(clusters[0]) > 9:

    # Figure out which 9 objects minimize area for each cluster.
    # Not the best approach to do this while removing the one that minimizes the area when removed
    # because it doesn't work for r1.
    for cluster in clusters:
        while len(cluster) > 9:
            minArea = 0
            minIndex = 0
            for index in range(len(cluster)):
                c = np.vstack(cluster[i][0] for i in range(len(cluster)) if i != index)
                hull = cv2.convexHull(c)
                #epsilon = 0.01 * cv2.arcLength(hull, True)
                #approx = cv2.approxPolyDP(hull, epsilon, True)
                area = cv2.contourArea(hull)
                if area < minArea:
                    minArea = area
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