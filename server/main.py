import json
from flask import Flask, request
from flask import render_template
from flask_cors import CORS, cross_origin

from src.libs import ConvBase64toImage, ConvImagetoBase64
from handle import url_process, image_process
from src.setting.config import config
from src.ocr.models import load_model 

PORT_SERVER = config.PORT_SERVER
HOST = config.HOST

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/app', methods=['POST'])
@cross_origin(origin='*')
def process_image():
    if request.method == 'POST':
        obj = request.form
        print("INFO: Get Request...")
        image_base64 = obj['img']
        lst = obj['lst']
        print(lst)
        lst = json.loads(lst)
        image = ConvBase64toImage(image_base64)
        image, text = image_process(detector = detector, reader = reader, image=image, lst=lst)
        image_base64 = ConvImagetoBase64(image)
        return {
                'image': image_base64,
                'text': text
                }
    else:
        return "Please use POST method"
            
@app.route('/debug', methods=['GET'])
@cross_origin(origin='*')
def process_url():
    if request.method == 'GET':
        url_drive = request.args.get('url', default=None, type=None)
        json_data = url_process(detector=detector, reader=reader, url_drive=url_drive)
        return json_data
        
@app.route('/', methods=['GET'])
@cross_origin(origin='*')
def get_index():
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    detector, reader = load_model()
    app.run(host=HOST, port=PORT_SERVER, debug=False)