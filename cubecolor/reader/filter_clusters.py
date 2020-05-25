import cv2
import numpy as np

def filterClusters(clusters):
        # Remove things with angle far from median
    for i in range(len(clusters)):
        cluster = clusters[i]
        if len(cluster) > 9:
            median = np.median([facelet[2] for facelet in cluster])
            clusters[i] = [facelet for facelet in cluster if abs(facelet[2] - median) < 10]

    # Figure out removing which object minimizes total distance from center, until there are 9 objects
    for cluster in clusters:
        while len(cluster) > 9:
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