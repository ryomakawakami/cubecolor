import cv2
import numpy as np
from scipy.spatial import ConvexHull

from cubecolor.reader.filter_image import filterImage
from cubecolor.reader.get_facelets import getFacelets
from cubecolor.reader.cluster_facelets import clusterFacelets
from cubecolor.reader.filter_clusters import filterClusters
from cubecolor.reader.identify_color import identifyColor
from cubecolor.reader.perp_bisector import clusterWithBisector
from cubecolor.reader.save_colors import saveColors

def reader(cube, inPath):
    image = cv2.imread(inPath, -1)

    filtered = filterImage(image)

    # Detect all contours
    contours, hierarchy = cv2.findContours(filtered, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    facelets = getFacelets(contours)

    # Cluster facelets based on angle
    clusters = clusterFacelets(facelets)
    if clusters == None:
        return 'E'

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

    # Identify each face. White/yellow is x, and y and z are cw from there
    hull = ConvexHull([center[3] for center in centers])
    centers = [centers[i] for i in hull.vertices]
    clusters = [clusters[i] for i in hull.vertices]
    i = 0
    whiteYellowIndex = 0
    for center in centers:
        if center[4] == 'w' or center[4] == 'y':
            whiteYellowIndex = i
            break
        i += 1
    # Roll array so that first is x, second is y, third is z
    if whiteYellowIndex == 1:
        centers = [centers[i] for i in [1, 2, 0]]
        clusters = [clusters[i] for i in [1, 2, 0]]
    if whiteYellowIndex == 2:
        centers = [centers[i] for i in [2, 0, 1]]
        clusters = [clusters[i] for i in [2, 0, 1]]

    # For AB_C, clusters on the C face from A and B face perp bisector
    # In order: XY_X XZ_X XY_Y YZ_Y XZ_Z YZ_Z
    facePositions = [
        clusterWithBisector(centers[0][3], centers[1][3], clusters[0]),
        clusterWithBisector(centers[0][3], centers[2][3], clusters[0]),
        clusterWithBisector(centers[0][3], centers[1][3], clusters[1]),
        clusterWithBisector(centers[1][3], centers[2][3], clusters[1]),
        clusterWithBisector(centers[0][3], centers[2][3], clusters[2]),
        clusterWithBisector(centers[1][3], centers[2][3], clusters[2])
    ]

    # Save colors in cube
    orientation = centers[0][4] + centers[1][4]
    saveColors(cube, facePositions, clusters, orientation)
