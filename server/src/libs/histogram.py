import cv2
from src.libs import read_show_data as rsd 

def histogram(image='', path='', debug=False, clipLimit=2.0, tileGridSize=(2,2)):
    if path:
        if debug:
            image = rsd.read(path)
        else:
            image = cv2.imread(path)
    
    original_image = image

    image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
    image[:,:,0] = clahe.apply(image[:,:,0])
    image = cv2.cvtColor(image, cv2.COLOR_YUV2BGR)

    if debug:
        rsd.show([original_image,image], ["Original","Histogram"])
    else:
        return image