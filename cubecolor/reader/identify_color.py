import cv2

colors = ['r', 'o', 'y', 'g', 'b', 'w']

def identifyColor(contour):
    masked_hsv = cv2.cvtColor(contour, cv2.COLOR_BGR2HSV)

    faceletContours = {}
    faceletContours['r'] = cv2.inRange(masked_hsv, (0, 100, 50), (10, 255, 255))    # Red
    faceletContours['o'] = cv2.inRange(masked_hsv, (10, 100, 50), (25, 255, 255))   # Orange
    faceletContours['y'] = cv2.inRange(masked_hsv, (27, 100, 50), (35, 255, 255))   # Yellow
    faceletContours['g'] = cv2.inRange(masked_hsv, (40, 100, 50), (80, 255, 255))   # Green
    faceletContours['b'] = cv2.inRange(masked_hsv, (80, 100, 50), (130, 255, 255))  # Blue
    faceletContours['w'] = cv2.inRange(masked_hsv, (0, 0, 100), (255, 20, 255))     # White

    maxArea = 0
    maxColor = 'w'  # Default case
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    for color in colors:
        # "Open" each filtered image and get contours
        morph = cv2.morphologyEx(faceletContours[color], cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if not contours:
            continue
        area = cv2.contourArea(max(contours, key = cv2.contourArea))

        if area > maxArea:
            maxArea = area
            maxColor = color

    return maxColor