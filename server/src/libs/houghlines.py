import cv2
import numpy as np
import matplotlib.pyplot as plt
from src.libs import read_show_data as rsd

def houghlines(image='', path='', debug=False):
    if path:
        if debug:
            image = rsd.read(path)
        else:
            image = cv2.imread(path)

    edge_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edge_image = cv2.GaussianBlur(edge_image, (5,5), 1) 
    edge_image = cv2.Canny(edge_image,180,200,apertureSize = 3)

    p = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 110  # minimum number of pixels making up a line
    max_line_gap = 10  # maximum gap in pixels between connectable line segments

    lines = cv2.HoughLinesP(edge_image, p, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(image,(x1,y1),(x2,y2),(0,255,0),5)

    if debug:
        rsd.show([image], ["Houghline"])
    else:
        return image