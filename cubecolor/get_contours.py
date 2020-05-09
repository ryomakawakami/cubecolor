import cv2
from find_corner import findCorner

def getContours(img, out):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # Get the outline of the cube
    max = contours[0]
    maxArea = cv2.contourArea(max)
    for contour in contours:
        area = cv2.contourArea(contour)
        
        if area > maxArea:
            maxArea = area
            max = contour

    hull = max

    # Find the convex hull of the outline (hopefully 6 points)
    epsilon = 0.02 * cv2.arcLength(hull, True)
    poly = cv2.approxPolyDP(hull, epsilon, True)
    hull = cv2.convexHull(poly)

    # Find corner point
    corner = []
    if len(hull) == 6:
        corner = findCorner(hull)

    # Draw points
    cv2.drawContours(out, hull, -1, (0, 0, 255), 10)
    if corner:
        cv2.circle(out, corner, 1, (255, 255, 255), 5)

    # Return visible vertices of cube
    points = list(tuple(pt[0]) for pt in hull)
    if corner:
        points.append(corner)
    return points