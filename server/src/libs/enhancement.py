import cv2
import numpy as np

def inc_brightness(image, brightness=40):
    temp = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(temp)
    lim = 255 - brightness
    v[v > lim] = 255
    v[v <= lim] += brightness
    temp = cv2.merge((h, s, v))
    image = cv2.cvtColor(temp, cv2.COLOR_HSV2BGR)
    return image

def dec_brightness(image, brightness=-40):
    temp = np.array(image)
    image = np.zeros_like(temp)
    image = temp + brightness
    image[image > 255] = 255
    image[image < 0] = 0
    return image.astype(np.uint8)

def inc_contract(image, contract=1.5, brightness=-70):
    temp = np.array(image)
    image = np.zeros_like(temp)
    image = (temp-0.5)*contract + 0.5 + brightness
    image = np.rint(image)
    image[image > 255] = 255
    image[image < 0] = 0
    return image.astype(np.uint8)

def dec_contrast(image, contract=0.5, brightness=50):
    temp = np.array(image)
    image = np.zeros_like(temp)
    image = (temp-0.5)*contract + 0.5 + brightness
    image = np.rint(image)
    image[image > 255] = 255
    image[image < 0] = 0
    return image.astype(np.uint8)

def Erosion(image, kernel_x=3, kernel_y=3):
    kernel = np.ones((kernel_x, kernel_y), np.uint8)
    image = cv2.erode(image, kernel)
    return image

def Dilation(image, kernel_x=3, kernel_y=3):
    kernel = np.ones((kernel_x, kernel_y), np.uint8)
    image = cv2.dilate(image, kernel)
    return image

def Opening(image, kernel_x=3, kernel_y=3):
    kernel = np.ones((kernel_x, kernel_y), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return image

def Closing(image, kernel_x=3, kernel_y=3):
    kernel = np.ones((kernel_x, kernel_y), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return image
    
def blur_bilateral(image, d=9, sigmaColor=50, sigmaSpace=50):
    image = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    return image