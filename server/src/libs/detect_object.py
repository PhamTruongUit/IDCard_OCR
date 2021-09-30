import cv2
import numpy as np
from src.libs import read_show_data as rsd
from src.libs import geometry
from src.libs import enhancement

def detect_object(image='', path='', debug=False, maxCornerNB=600, qualityLevel=0.05, minDistance=0.6):
    if path:
        if debug:
            image = rsd.read(path)
        else:
            image = cv2.imread(path)

    # corner detector
    corners = auto_corners(image)

    # index crop image
    x_min = np.amin(corners[:,0])
    x_max = np.amax(corners[:,0])
    y_min = np.amin(corners[:,1])
    y_max = np.amax(corners[:,1])

    if debug:
        for indexs in corners:
            x, y = indexs
            cv2.circle(image, (x, y), 7, (0, 255, 0), -1)
        rsd.show([image], ["corner detector"], figsize=(10,7))
    else:
        return image[y_min:y_max, x_min:x_max]

def auto_corners(image):
    contract = 1.5
    brightness = -20
    scale_weight = 0.4
    # increase contract and decrease brightness
    image = enhancement.contract_brightness(image, contract=contract, brightness=brightness)
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