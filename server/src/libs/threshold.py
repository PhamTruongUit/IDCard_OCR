import cv2
import numpy as np
from src.libs import read_show_data as rsd

def threshold(image='', path='', mode='RGB', debug=False, low_color=[0,0,0], high_color=[255,255,255]):
    if path:
        if debug:
            image = rsd.read(path)
        else:
            image = cv2.imread(path)

    lower_blue = np.array(low_color)
    upper_blue = np.array(high_color)

    if mode == 'HSV':
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,lower_blue, upper_blue)
    elif mode == 'RGB':
        mask = cv2.inRange(image,lower_blue, upper_blue)
    
    result = cv2.bitwise_and(image,image,mask = mask)
    
    if debug:
        rsd.show([mask,result], ["mask","result"])
    else:
        return mask,result