import cv2

# Filter out small and non-solid contours, and save as facelets
def getFacelets(contours):
    facelets = []
    for contour in contours:
        area = cv2.contourArea(contour)
        hull = cv2.convexHull(contour)
        hull_area = cv2.contourArea(hull)
        solidity = float(area)/hull_area

        if area < 600 or area > 6500 or solidity < 0.9:
            continue

        (x,y), (MA,ma), angle = cv2.fitEllipse(contour)
        
        M = cv2.moments(contour)
        cx = (int) (M['m10'] / M['m00'])
        cy = (int) (M['m01'] / M['m00'])

        facelets.append([contour, area, angle, (cx, cy)])

    return facelets