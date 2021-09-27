import cv2
import numpy as np

def nothing(x):
    pass

def rgpColor(path):
    # Creating a window for later use
    cv2.namedWindow('tool',cv2.WINDOW_NORMAL)
    # Starting with 100's to prevent error while masking
    R_low,G_low,B_low,R_high,G_high,B_high = 0,0,0,255,255,255
    
    # Creating track bar
    cv2.createTrackbar('R_low', 'tool',0,255,nothing)
    cv2.createTrackbar('G_low', 'tool',0,255,nothing)
    cv2.createTrackbar('B_low', 'tool',0,255,nothing)

    cv2.createTrackbar('R_high', 'tool',255,255,nothing)
    cv2.createTrackbar('G_high', 'tool',255,255,nothing)
    cv2.createTrackbar('B_high', 'tool',255,255,nothing) 
    
    while(path):
        frame = cv2.imread(path)

        # get info from track bar and appy to result
        R_low = cv2.getTrackbarPos('R_low','tool')
        G_low = cv2.getTrackbarPos('G_low','tool')
        B_low = cv2.getTrackbarPos('B_low','tool')
        
        R_high = cv2.getTrackbarPos('R_high','tool')
        G_high = cv2.getTrackbarPos('G_high','tool')
        B_high = cv2.getTrackbarPos('B_high','tool')
        
        # Normal masking algorithm
        lower_blue = np.array([R_low,G_low,B_low])
        upper_blue = np.array([R_high,G_high,B_high])
        mask = cv2.inRange(frame,lower_blue, upper_blue)

        cv2.imshow('mask',mask)
        result = cv2.bitwise_and(frame,frame,mask = mask)
        cv2.imshow('result',result)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()