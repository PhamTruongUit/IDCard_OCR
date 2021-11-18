import cv2
import numpy as np
from src.libs import geometry
from src.libs import enhancement

def auto_corners(image, contrast = 1.5, brightness = -20, scale_weight = 0.4):
    # increase contrast and decrease brightness
    image = enhancement.inc_contract(image, contrast=contrast, brightness=brightness)
    image = geometry.scale(image, weight=scale_weight)
    new_height, new_width, _ = image.shape

    # USE BILATERAL FILTER TO REDUCE NOISE BUT ALSO PRESERVE EDGES
    image = cv2.bilateralFilter(image, 7, 121, 121)

    # APPLY CANNY EDGE DETECTOR (NEED MORE EXPLANATION)
    imgThreshold = cv2.Canny(image, 9, 50)

    # APPLY Morphological Operations
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgThreshold, kernel, iterations=2)  # APPLY DILATION
    imgThreshold = cv2.erode(imgDial, kernel, iterations=1)  # APPLY EROSION

    # FIND ALL CONTOURS
    contours, _ = cv2.findContours(
        imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # FIND BIGGEST CONTOUR (CONTAINS 4 MAIN CORNERS)
    biggest = np.array(
        [[0, 0], [new_width, 0], [new_width, new_height], [0, new_height]]
    )  # Default contour if no contour is found
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        peri = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.03 * peri, True)
        if area > max_area and len(approx) == 4:
            biggest = approx
            max_area = area

    biggest = biggest.reshape((4, 2))

    # SORT CORNERS AND RESCALE THEM
    corners = sort_corners(biggest) * (1 / scale_weight)
    return corners.astype(np.intc)

def sort_corners(corners):
    assert corners.shape == (4, 2)
    diff = np.diff(corners, axis=1)
    total = corners.sum(axis=1)
    # Top-left point has smallest sum...
    return np.array(
        [
            corners[np.argmin(total)],
            corners[np.argmin(diff)],
            corners[np.argmax(total)],
            corners[np.argmax(diff)],
        ]
    )