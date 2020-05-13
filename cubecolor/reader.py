import cv2
import numpy as np
import os

from filter_image import filterImage
from get_facelets import getFacelets
from cluster_facelets import clusterFacelets
from filter_clusters import filterClusters
from identify_color import identifyColor

imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
inPath = os.path.join(imageDir, 'r2.jpg')

image = cv2.imread(inPath, -1)

#vid = cv2.VideoCapture(0)

while True:
    #_, image = vid.read()
    imCopy = image.copy()

    filtered = filterImage(image)

    # Detect all contours
    contours, hierarchy = cv2.findContours(filtered, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    facelets = getFacelets(contours)

    # Cluster facelets based on angle
    clusters = clusterFacelets(facelets)

    # Filter the 3 clusters to 9 facelets each
    filterClusters(clusters)

    i = 0
    for cluster in clusters:
        j = 0
        for facelet in cluster:
            hull = cv2.convexHull(facelet[0])
            mask = np.zeros(image.shape, np.uint8)
            cv2.fillConvexPoly(mask, hull, (255, 255, 255))
            masked = cv2.bitwise_and(image, mask)
            
            color = identifyColor(masked)
            clusters[i][j].append(color)

            j += 1
        i += 1

    # Display
    i = 0
    for cluster in clusters:
        for facelet in cluster:
            color = (0, 0, 0)
            #if i == 0:
            #    color = (255, 0, 0)
            #elif i == 1:
            #    color = (0, 255, 0)
            #else:
            #    color = (0, 0, 255)

            cx, cy = facelet[3]

            cv2.putText(imCopy, facelet[4], (cx - 13, cy + 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, color)
        i += 1

    cv2.imshow('image', imCopy)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey()
cv2.destroyAllWindows()
