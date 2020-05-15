import numpy as np
from scipy.cluster.vq import kmeans, vq

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
    arr = []
    for facelet in face:
        point = np.asarray(facelet[3])
        arr.append(np.linalg.norm(np.cross(b1 - b0, b0 - point)) / np.linalg.norm(b1 - b0))

    # Cluster by distance
    codebook, _ = kmeans(arr, 3)
    cluster_indices, _ = vq(arr, codebook)
    cluster_indices = [i for i in cluster_indices]

    # Make 0 the closest cluster and 2 the farthest cluster
    conv = {0: 1, 1: 1, 2: 1}
    first = [cluster_indices.index(i) for i in range(3)]
    a = [arr[i] for i in first]   # Simplify dist arr to representatives

    far = arr.index(max(a))       # Get index of max distance cluster
    farIndex = first.index(far)
    conv[farIndex] = 2
    
    close = arr.index(min(a))       # Get index of min distance cluster
    closeIndex = first.index(close)
    conv[closeIndex] = 0

    cluster_indices = [conv[i] for i in cluster_indices]

    return cluster_indices
