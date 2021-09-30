import cv2
import numpy as np
from src.libs import read_show_data as rsd

def corner_detector(image='', path='', debug=False, maxCornerNB=600, qualityLevel=0.05, minDistance=0.6):
    if path:
        if debug:
            image = rsd.read(path)
        else:
            image = cv2.imread(path)
    # convert to gray image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # shi tomasi detect corners
    corners = cv2.goodFeaturesToTrack(gray, maxCornerNB, qualityLevel, minDistance)
    corners = np.int0(corners)

    for i in corners:
        # take (x, y) of corners
        x, y = i.ravel()
        # draw circle
        cv2.circle(image, (x, y), 3, (0, 0, 255), -1)

    if debug:
        rsd.show([image], ["corner detector"])
    else:
        return image