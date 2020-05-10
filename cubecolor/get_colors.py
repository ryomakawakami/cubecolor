import cv2

colors = ['r', 'o', 'y', 'g', 'b', 'w']

# Returns array of positions and colors of facelets
def getColors(masked, image):
    # Convert to HSV
    masked_hsv = cv2.cvtColor(masked, cv2.COLOR_BGR2HSV)

    # Filter for each color
    faceletContours = {}
    faceletContours['r'] = cv2.inRange(masked_hsv, (0, 100, 50), (10, 255, 255))    # Red
    faceletContours['o'] = cv2.inRange(masked_hsv, (10, 100, 50), (25, 255, 255))   # Orange
    faceletContours['y'] = cv2.inRange(masked_hsv, (27, 100, 50), (35, 255, 255))   # Yellow
    faceletContours['g'] = cv2.inRange(masked_hsv, (40, 100, 50), (80, 255, 255))   # Green
    faceletContours['b'] = cv2.inRange(masked_hsv, (80, 100, 50), (130, 255, 255))  # Blue
    faceletContours['w'] = cv2.inRange(masked_hsv, (0, 0, 100), (255, 20, 255))     # White

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    contours = []
    facelets = []
    for color in colors:
        # "Open" each filtered image and get contours
        morph = cv2.morphologyEx(faceletContours[color], cv2.MORPH_OPEN, kernel)
        c, hierarchy = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        for contour in c:
            # Check if facelet
            area = cv2.contourArea(contour)
            per = cv2.arcLength(contour, True)
            if area < 800 or per > 1500:
                continue

            contours.append(contour)
            
            # Find centroid
            M = cv2.moments(contour)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            # Add to be returned
            facelets.append([cx, cy, color])

    cv2.drawContours(image, contours, -1, (0, 0, 255), 3)

    for facelet in facelets:
        cv2.putText(image, facelet[2], (facelet[0] - 13, facelet[1] + 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

    return facelets