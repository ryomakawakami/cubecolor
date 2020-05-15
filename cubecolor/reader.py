import cv2
import numpy as np
from scipy.spatial import ConvexHull
import os

from filter_image import filterImage
from get_facelets import getFacelets
from cluster_facelets import clusterFacelets
from filter_clusters import filterClusters
from identify_color import identifyColor
from perp_bisector import clusterWithBisector

imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
inPath = os.path.join(imageDir, 'r1.jpg')

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

    # Label colors
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

    # Find center pieces
    centers = []
    for cluster in clusters:
        # Find CM
        sum = [0, 0]
        for facelet in cluster:
            sum[0] += facelet[3][0]
            sum[1] += facelet[3][1]
        mid = [sum[0] / 9, sum[1] / 9]

        # Find closest to CM. This is center piece
        c = cluster[0]
        minD = 1000000
        for facelet in cluster:
            dX = facelet[3][0] - mid[0]
            dY = facelet[3][1] - mid[1]
            d = dX * dX + dY * dY
            if d < minD:
                minD = d
                c = facelet
        centers.append(c)

    # Identify each face. Top is U, left is F, right is R (in standard view)
    hull = ConvexHull([center[3] for center in centers])
    centers = [centers[i] for i in hull.vertices]
    clusters = [clusters[i] for i in hull.vertices]
    i = 0
    topIndex = 0
    topY = 1000000
    for center in centers:
        if center[3][1] < topY:
            topIndex = i
            topY = center[3][1]
        i += 1
    # Roll array so that first is U, second is R, third is F
    if topIndex == 1:
        centers = [centers[i] for i in [1, 2, 0]]
        clusters = [clusters[i] for i in [1, 2, 0]]
    if topIndex == 2:
        centers = [centers[i] for i in [2, 0, 1]]
        clusters = [clusters[i] for i in [2, 0, 1]]

    # For AB_C, clusters on the C face from A and B face perp bisector
    clusterUR_U = clusterWithBisector(centers[0][3], centers[1][3], clusters[0])
    clusterUR_R = clusterWithBisector(centers[0][3], centers[1][3], clusters[1])

    i = 0
    for facelet in clusters[0]:
        color = ()
        if clusterUR_U[i] == 0:
            color = (255, 0, 0)
        elif clusterUR_U[i] == 1:
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)
        cv2.circle(imCopy, facelet[3], 2, color, 5)
        i += 1

    # Display
    for cluster in clusters:
        for facelet in cluster:
            color = (0, 0, 0)
            cx, cy = facelet[3]
            cv2.putText(imCopy, facelet[4], (cx - 13, cy + 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, color)

    cv2.imshow('image', imCopy)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey()
cv2.destroyAllWindows()
