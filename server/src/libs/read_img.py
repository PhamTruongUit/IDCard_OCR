import cv2

def read_img(posixpath, gray=False):
    # opencv read img with BGR
    raw_img = cv2.imread(str(posixpath))
    if gray:
        return cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
    # if opencv==False:
    return cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB)