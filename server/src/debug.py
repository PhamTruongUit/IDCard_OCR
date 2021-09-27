import os
import sys
import cv2
from tools.HSV import hsvColor
from tools.RGP import rgpColor
from libs.threshold import threshold
from setting.config import config
from api.OCRfree import ocr_file, ocr_url

API_KEY = config.API_KEY
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = 'test03.jpg'
path = os.path.join(ROOT_DIR,'images',file_name)

# rgpColor(path)

# hsvColor(path)

# threshold(path, 
#             mode='RGB', 
#             debug=True, 
#             low_color=[0,0,0], 
#             high_color=[255,255,255])

# print(ocr_file(path, api_key = API_KEY))
