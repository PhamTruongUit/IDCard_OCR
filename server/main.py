import json
from flask import Flask, request
from flask import render_template, jsonify
from flask_cors import CORS, cross_origin

from src.libs import ConvBase64toImage, ConvImagetoBase64
from handle import url_process, image_process
from src.setting.config import config

PORT = config.PORT
HOST = config.HOST

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/app', methods=['POST'])
@cross_origin(origin='*')
def main_process():
    obj = request.form
    image_base64 = obj['img']
    lst = obj['lst']
    # print(lst)
    lst = json.loads(lst)
    image = ConvBase64toImage(image_base64)
    image, text = image_process(image=image, lst=lst)
    image_base64 = ConvImagetoBase64(image)
    return {
            'image': image_base64,
            'text': text
            }

@app.route('/', methods=['GET'])
@cross_origin(origin='*')
def get_index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/debug', methods=['GET'])
@cross_origin(origin='*')
def url_process():
    if request.method == 'GET':
        # url_drive = request.args.get('url', default=None, type=None)
        # json_data = url_process(url_drive)
        json_data = {
            "123": "trường",
            "456": "Thịnh"
        }
        return json_data

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)