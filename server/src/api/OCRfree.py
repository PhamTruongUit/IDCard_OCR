import requests
import json

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
