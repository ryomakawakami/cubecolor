import cv2
import numpy as np
import os

def empty(_):
    pass

imageDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
inPath = os.path.join(imageDir, 's1.jpg')

img = cv2.imread(inPath, -1)

vid = cv2.VideoCapture(0)

while True:
    _, img = vid.read()

    rgb_planes = cv2.split(img)

    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        result_planes.append(diff_img)
        result_norm_planes.append(norm_img)

    result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)

    gray = cv2.cvtColor(result_norm, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 59, 36)

    kernel = np.ones((5, 5))
    dilated = cv2.dilate(canny, kernel, iterations = 1)

    cv2.imshow('dilated', canny)
    cv2.imshow('test', img)
    cv2.imshow('shadows_out_norm.png', result_norm)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break