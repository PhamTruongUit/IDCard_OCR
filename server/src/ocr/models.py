import easyocr
from vietocr.tool.config import Cfg
from vietocr.tool.predictor import Predictor
from src.setting.config import config

def load_model():
    DEVICE = config.DEVICE
    WEIGHT = config.WEIGHT

    print('INFO: Loading model...')
    # vietocr
    custom = Cfg.load_config_from_name('vgg_transformer')
    custom['cnn']['pretrained']=False
    custom['predictor']['beamsearch']=False
    custom['device'] = DEVICE
    custom['weights'] = WEIGHT
    detector = Predictor(custom)

    # easyocr
    reader = easyocr.Reader(['vi'])
    return detector, reader