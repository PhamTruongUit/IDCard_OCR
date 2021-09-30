import cv2

def scale(image, weight, interpolation = cv2.INTER_CUBIC):
    m,n,_ = image.shape
    dsize = (round(n*weight),round(m*weight))
    return cv2.resize(image, dsize, 0, 0, interpolation=interpolation)

def rotate(image, angle = 0, scale=1, flags=cv2.INTER_CUBIC):
    m,n,_ = image.shape
    dsize = (n,m)
    center = (n/2, m/2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=scale)
    return cv2.warpAffine(image, M=rotate_matrix, dsize=dsize, flags=flags)