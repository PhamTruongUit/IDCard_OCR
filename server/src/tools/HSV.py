import cv2
import numpy as np

def nothing(x):
    pass

def hsvColor(path):
    # Creating a window for later use
    cv2.namedWindow('tool',cv2.WINDOW_NORMAL)
    # Starting with 100's to prevent error while masking    
    H_low,S_low,V_low,H_high,S_high,V_high = 0,0,0,180,255,255

    # Creating track bar
    cv2.createTrackbar('H_low', 'tool',0,180,nothing)
    cv2.createTrackbar('S_low', 'tool',0,255,nothing)
    cv2.createTrackbar('V_low', 'tool',0,255,nothing)
    cv2.createTrackbar('H_high', 'tool',180,180,nothing)
    cv2.createTrackbar('S_high', 'tool',255,255,nothing)
    cv2.createTrackbar('V_high', 'tool',255,255,nothing)

    while(path):
        frame = cv2.imread(path)
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # get info from track bar and appy to result
        H_low = cv2.getTrackbarPos('H_low','tool')
        S_low = cv2.getTrackbarPos('S_low','tool')
        V_low = cv2.getTrackbarPos('V_low','tool')

        H_high = cv2.getTrackbarPos('H_high','tool')
        S_high = cv2.getTrackbarPos('S_high','tool')
        V_high = cv2.getTrackbarPos('V_high','tool')

        # Normal masking algorithm
        lower_blue = np.array([H_low,S_low,V_low])
        upper_blue = np.array([H_high,S_high,V_high])
        mask = cv2.inRange(hsv,lower_blue, upper_blue)
        cv2.imshow('mask',mask)
        result = cv2.bitwise_and(frame,frame,mask = mask)
        cv2.imshow('result',result)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()