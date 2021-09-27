import cv2
import numpy as np
from libs.read_img import read_img
from libs.show_imgs import show_imgs

def threshold(path, mode='RGB', debug=False, low_color=[], high_color=[]):
    if debug:
        image = read_img(path)
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
        show_imgs([mask,result], ["mask","result"])
    else:
        return mask,result