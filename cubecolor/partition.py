from scipy.spatial import ConvexHull
import numpy as np
import math

def dist(x1,y1, x2,y2, x3,y3): # x3,y3 is the point
    px = x2-x1
    py = y2-y1

    something = px*px + py*py

    u =  ((x3 - x1) * px + (y3 - y1) * py) / float(something)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = x1 + u * px
    y = y1 + u * py

    dx = x - x3
    dy = y - y3

    #dist = math.sqrt(dx*dx + dy*dy)
    dist = dx * dx + dy * dy

    return dist

def distToHull(p, hull):
    dists=[]
    for i in range(len(hull) - 1):
        dists.append(dist(hull[i][0], hull[i][1], hull[i+1][0], hull[i+1][1], p[0], p[1]))
    d = min(dists)

    return d

def removeOuter(facelets):
    hull = ConvexHull(facelets)

    hullPoints = [facelets[i] for i in hull.vertices]
    outer = []
    realHullPoints = []
    realHull = []
    for i in range(len(facelets)):
        if distToHull(facelets[i], hullPoints) < 625:
            outer.append([facelets[i, 0], facelets[i, 1]])
            realHullPoints.append(i)

    for i in reversed(sorted(realHullPoints)):
        facelets = np.delete(facelets, (i), axis = 0)

    return outer, facelets

def removeLayer(facelets):
    hull = ConvexHull(facelets)

    hullPoints = [[facelets[i, 0], facelets[i, 1]] for i in hull.vertices]

    for i in reversed(sorted(hull.vertices)):
        facelets = np.delete(facelets, (i), axis = 0)

    return hullPoints, facelets

def partition(facelets):
    outer, facelets = removeOuter(facelets)     # Special case since 3 points per theoretical edge
    middle, facelets = removeLayer(facelets)
    inner, facelets = removeLayer(facelets)

    return inner, middle, outer
