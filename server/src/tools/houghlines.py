import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

def houghlines(path):
    # Creating a window for later use
    cv2.namedWindow('tool',cv2.WINDOW_NORMAL)

    # Creating track bar
    cv2.createTrackbar('p', 'tool',1,50,nothing)
    cv2.createTrackbar('threshold', 'tool',1,500,nothing)
    cv2.createTrackbar('min_line_length', 'tool',1,500,nothing)
    cv2.createTrackbar('max_line_gap', 'tool',1,500,nothing)

    cv2.createTrackbar('low_canny', 'tool',0,255,nothing)
    cv2.createTrackbar('high_canny', 'tool',255,255,nothing)

    p = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 110  # minimum number of pixels making up a line
    max_line_gap = 10  # maximum gap in pixels between connectable line segments

    while(path):
        frame = cv2.imread(path)
        edge_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edge_image = cv2.GaussianBlur(edge_image, (5,5), 1) 

        # get info from track bar and appy to result
        p               = cv2.getTrackbarPos('p','tool')
        threshold       = cv2.getTrackbarPos('threshold','tool')
        min_line_length = cv2.getTrackbarPos('min_line_length','tool')
        max_line_gap    = cv2.getTrackbarPos('max_line_gap','tool')
        low_canny       = cv2.getTrackbarPos('low_canny','tool')
        high_canny      = cv2.getTrackbarPos('high_canny','tool')

        edge_image = cv2.Canny(edge_image,low_canny,high_canny,apertureSize = 3)

        lines = cv2.HoughLinesP(edge_image, p, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
        cv2.imshow('edge_image',edge_image)
        cv2.imshow('result',frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()