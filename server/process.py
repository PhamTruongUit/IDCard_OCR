import src.libs as libs
from src.setting.config import config
from src.api.ocr import ocr_image 

API_KEY = config.API_KEY
LANGUAGE = config.LANGUAGE

def process(image,lst=[]):
    # pre processing
    image = image_processing(image,lst)
    # call API
    text = OCR(image)

    return image, text

def image_processing(image, lst=[]):
    if lst:
        print(lst)
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
    return image

def OCR(image):
    return ocr_image(image, api_key=API_KEY, language=LANGUAGE)