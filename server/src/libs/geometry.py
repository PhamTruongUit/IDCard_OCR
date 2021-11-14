import cv2
import numpy as np
from scipy.ndimage import interpolation as inter

def scale(image, weight, interpolation = cv2.INTER_CUBIC):
    m,n,_ = image.shape
    dsize = (round(n*weight),round(m*weight))
    image = cv2.resize(image, dsize, 0, 0, interpolation=interpolation)
    return image

def rotate(image, angle = 0, scale=1, flags=cv2.INTER_CUBIC):
    m,n,_ = image.shape
    dsize = (n,m)
    center = (n/2, m/2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=scale)
    image = cv2.warpAffine(image, M=rotate_matrix, dsize=dsize, flags=flags)
    return image

def determine_score(thresh, angle):
    data = inter.rotate(thresh, angle, reshape=False, order=0)
    histogram = np.sum(data, axis=1)
    score = np.sum((histogram[1:] - histogram[:-1]) ** 2)
    return score

def auto_rotation(image, delta=1, limit=10):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 
    scores = []
    angles = np.arange(-limit, limit + delta, delta)
    
    for angle in angles:
        score = determine_score(thresh, angle)
        scores.append(score)

    best_angle = angles[scores.index(max(scores))]
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, best_angle, 1.0)

    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, \
              borderMode=cv2.BORDER_REPLICATE)

    return rotated