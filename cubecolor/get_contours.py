import cv2
import numpy as np

def getContours(img, out):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Get the outline of the cube
    if not contours:
        return
    max = contours[0]
    maxArea = cv2.contourArea(max)
    for contour in contours:
        area = cv2.contourArea(contour)
        
        if area > maxArea:
            maxArea = area
            max = contour

    hull = max
    
    #cv2.drawContours(out, max, -1, (0, 0, 255), 10)

    # Find the convex hull of the outline (hopefully 6 points)
    epsilon = 0.02 * cv2.arcLength(hull, True)
    poly = cv2.approxPolyDP(hull, epsilon, True)
    hull = cv2.convexHull(poly)

    mask = np.zeros(img.shape, np.uint8)
    cv2.fillConvexPoly(mask, hull, (255, 255, 255))

    # Draw points
    cv2.drawContours(out, hull, -1, (0, 0, 255), 10)

    return mask