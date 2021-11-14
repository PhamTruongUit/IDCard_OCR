import easyocr
from vietocr.tool.config import Cfg
from vietocr.tool.predictor import Predictor

def load_model():
    print('INFO: Loading model...')
    # vietocr
    custom = Cfg.load_config_from_name('vgg_transformer')
    custom['cnn']['pretrained']=False
    custom['predictor']['beamsearch']=False
    custom['device'] = 'cpu'
    custom['weights'] = './src/ocr/transformerocr.pth'
    # custom['device'] = 'cuda:0'
    # custom['weights'] = 'https://drive.google.com/uc?id=13327Y1tz1ohsm5YZMyXVMPIOjoOA0OaA'
    detector = Predictor(custom)

    # easyocr
    reader = easyocr.Reader(['vi'])
    return detector, reader