import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
    pass

def corner_detector(path):
    # Creating a window for later use
    cv2.namedWindow('tool',cv2.WINDOW_NORMAL)

    # Creating track bar
    cv2.createTrackbar('maxCornerNB', 'tool',600,1000,nothing)
    cv2.createTrackbar('qualityLevel*100', 'tool',5,1000,nothing)
    cv2.createTrackbar('minDistance*100', 'tool',60,1000,nothing)

    maxCornerNB     = 600 
    qualityLevel    = 0.05
    minDistance     = 0.6

    while(path):
        frame = cv2.imread(path)

        maxCornerNB     = cv2.getTrackbarPos('maxCornerNB','tool')
        qualityLevel    = cv2.getTrackbarPos('qualityLevel*100','tool')/100
        minDistance     = cv2.getTrackbarPos('minDistance*100','tool')/100

        # convert to gray image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # shi tomasi detect corners
        corners = cv2.goodFeaturesToTrack(gray, maxCornerNB, qualityLevel, minDistance)
        corners = np.int0(corners)

        for i in corners:
            # take (x, y) of corners
            x, y = i.ravel()
            # draw circle
            cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)

        cv2.imshow('result',frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()