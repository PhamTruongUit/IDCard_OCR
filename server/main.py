from flask import Flask, request
from flask_cors import CORS, cross_origin

from src.libs import ConvBase64toImage, ConvImagetoBase64
from process import process
from src.setting.config import config

PORT_SERVER = config.PORT_SERVER
HOST = config.HOST

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/app', methods=['POST'])
@cross_origin(origin='*')
def main_process():
    obj = request.form.get()
    image_base64 = obj['image']
    lst = obj['lst']
    image = ConvBase64toImage(image_base64)
    image, text = process(image, lst)
    image_base64 = ConvImagetoBase64(image)
    return {
            'image': image_base64,
            'text': text
            }

@app.route('/', methods=['GET'])
@cross_origin(origin='*')
def index():
    return "Hello day la server Python"

if __name__ == '__main__':
    app.run(host=HOST, port=PORT_SERVER, debug=False)