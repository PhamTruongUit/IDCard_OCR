import cv2
import base64
import numpy as np

def ConvBase64toImage(image_base64):
    try:
        image = np.fromstring(base64.b64decode(image_base64), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_ANYCOLOR)
        return image
    except:
        return None

def ConvImagetoBase64(image):
    try:
        image = cv2.imencode('.jpg', image)[1]
        image_base64 = base64.b64encode(image).decode()
        return image_base64
    except:
        return image