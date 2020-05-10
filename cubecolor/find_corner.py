import numpy as np

# Get intersection of line(p1, p2) and line(p3, p4)
def getIntersection(p1, p2, p3, p4):
    d = (p4[1] - p3[1]) * (p2[0] - p1[0]) - (p4[0] - p3[0]) * (p2[1] - p1[1])
    if d != 0:
        uA = ((p4[0] - p3[0]) * (p1[1] - p3[1]) - (p4[1] - p3[1]) * (p1[0] - p3[0])) / d
        uB = ((p2[0] - p1[0]) * (p1[1] - p3[1]) - (p2[1] - p1[1]) * (p1[0] - p3[0])) / d
    else:
        return

    x = p1[0] + uA * (p2[0] - p1[0])
    y = p1[1] + uA * (p2[1] - p1[1])

    return x, y

# Pass in ndarray of 6 ccw vertices of convex hull
# Returns approximate position of corner within the hull
def findCorner(pts):
    # Find top point
    topY = 0
    topIndex = 0
    for i in range(0, 5):
        if pts[i][0][1] < topY:
            topY = pts[i][0][1]
            topIndex = i

    # Roll array so top point is last
    np.roll(pts, 5 - topIndex)

    # Convert to easier access
    v = list(list(pt[0]) for pt in pts)

    # Let line0 be line(v[0], v[1]), line1 be line(v[1], v[2]), and so on
    # a is the intersection of line 1 and line 4
    # b is line 0 and line 3
    # c is line 2 and line 5
    a = getIntersection(v[1], v[2], v[4], v[5])
    b = getIntersection(v[0], v[1], v[3], v[4])
    c = getIntersection(v[2], v[3], v[5], v[0])

    # We want the approximate intersection of line(a, v[0]), line(b, v[2]), line(c, v[4])
    a0b2 = getIntersection(a, v[0], b, v[2])
    a0c4 = getIntersection(a, v[0], c, v[4])
    b2c4 = getIntersection(b, v[2], c, v[4])
    avgX = int((a0b2[0] + a0c4[0] + b2c4[0]) / 3)
    avgY = int((a0b2[1] + a0c4[1] + b2c4[1]) / 3)
    return avgX, avgY
