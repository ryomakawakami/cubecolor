import numpy as np

def getBisector(p0, p1):
    slope = (p1[1] - p0[1]) / (p1[0] - p0[0])

    xm = (p0[0] + p1[0]) / 2.0
    ym = (p0[1] + p1[1]) / 2.0

    x1 = 0
    y1 = xm / slope + ym

    return (xm, ym), (x1, y1)

def clusterWithBisector(c0, c1, face):
    # Get perp bisector
    b0, b1 = getBisector(c0, c1)
    b0 = np.asarray(b0)
    b1 = np.asarray(b1)

    # Determine each distance
    arr = np.empty(9)
    i = 0
    for facelet in face:
        point = np.asarray(facelet[3])
        arr[i] = np.linalg.norm(np.cross(b1 - b0, b0 - point)) / np.linalg.norm(b1 - b0)
        i += 1

    # Cluster by distance
    arr = np.argsort(np.argsort(arr))
    cluster_indices = [int(x / 3) for x in arr]

    return cluster_indices
