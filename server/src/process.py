from server.src.debug import API_KEY
import api
import libs
from setting.config import config

API_KEY = config.API_KEY
LANGUAGE = config.LANGUAGE

def process(image,lst=[]):
    # image processing
    if lst[0] == 'auto':
        # option auto
        None
    else:
        for attribute in lst:
            # call function libs.attribute()
            try:
                image = getattr(libs,attribute)(image)
            except:
                None
    # call API
    text = OCR(image)
    
    return image, text

def OCR(image):
    return api.ocr_file(image, api_key=API_KEY, language=LANGUAGE)