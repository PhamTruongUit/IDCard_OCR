from src import libs
from src.setting.config import config
from src.ocr import ocr_custom
from src.api.ocr import ocr_image

def process(image, lst=[]):
    
    # pre processing
    image = image_processing(image, lst)
    # call API
    # text = OCR(image)
    # text = "chay thu ne he"

    # call model
    text = ocr_custom(image, debug=False)

    return image, text


def image_processing(image, lst=[]):
    if lst:
        if lst[0] == 'none':
            None      
        elif lst[0] == 'auto':
            image = getattr(libs, "detect_object")(image)
            image = getattr(libs, "contract_brightness")(image)
        else:
            # image processing
            for attribute in lst:
                # call function libs.attribute()
                try:
                    image = getattr(libs, attribute)(image)
                except:
                    None
    return image


def OCR(image):
    API_KEY = config.API_KEY
    LANGUAGE = config.LANGUAGE
    texts = ocr_image(image, api_key=API_KEY, language=LANGUAGE)
    return texts
