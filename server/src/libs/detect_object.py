import cv2
import numpy as np
from src.libs import read_show_data as rsd
from src.libs.corners_detector import auto_corners

def detect_object(image='', path='', debug=False):
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