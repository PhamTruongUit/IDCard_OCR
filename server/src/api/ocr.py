import requests
import json
import cv2
import base64

def ocr_image(image, overlay=False, api_key="helloworld", language='eng'):
    #convert ndarray to base 64
    encode_base64 = base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()
    data_base64 = f'data:image/jpeg;base64,{encode_base64}'
    
    payload = {'isOverlayRequired': overlay,
               'base64Image': data_base64,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                        data=payload,
                        )
    return json.loads(r.content.decode())["ParsedResults"][0]["ParsedText"]

def ocr_file(filename, overlay=False, api_key="helloworld", language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return json.loads(r.content.decode())["ParsedResults"][0]["ParsedText"]


def ocr_url(url, overlay=False, api_key="helloworld", language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return json.loads(r.content.decode())["ParsedResults"][0]["ParsedText"]