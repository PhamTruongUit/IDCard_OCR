import src.ocr as ocr
import easyocr
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import matplotlib.pyplot as plt
from src.libs.read_show_data import show
from src.setting.config import config

def lst_show(lst_lines, figsize=(16, 10)):
    l = len(lst_lines)
    fig = plt.figure(num = "Result", figsize=figsize)
    for i in range(1, l+1):
        img = lst_lines[i-1]
        fig.add_subplot(l, 1, i)
        plt.imshow(img)
    plt.show()

def check_fields(texts):
    temp = ocr.format_text(texts)
    result = []
    FIELDS = config.FIELDS
    for i in range(len(texts)):
        if ocr.search_custom(temp[i], FIELDS):
            result.append(texts[i])
    return result

def ocr_custom(image, debug=False):
    lst_start = config.START
    lst_end = config.END

    custom = Cfg.load_config_from_name('vgg_transformer')
    custom['cnn']['pretrained']=False
    custom['predictor']['beamsearch']=False
    custom['weights'] = './src/ocr/transformerocr.pth'
    custom['device'] = 'cpu'
    # custom['weights'] = 'https://drive.google.com/uc?id=13327Y1tz1ohsm5YZMyXVMPIOjoOA0OaA'
    # custom['device'] = 'cuda:0'
    reader = easyocr.Reader(['vi'])
    detector = Predictor(custom)

    bounds = reader.readtext(image, flag = True)
    box = ocr.boxes_line(bounds)
    lst_lines = ocr.crop_lines(image, box)
    lst_text = ocr.OCR(lst_lines, detector)
    # print(lst_text)

    pos_start = ocr.index_line(lst_text, 0, lst_start)
    pos_end = ocr.index_line(lst_text, 1, lst_end)

    if debug:
        box_temp = box[pos_start:pos_end+1]
        position = ocr.cluster_paragraph(box_temp)
        texts = lst_text[pos_start:pos_end+1]
        texts = check_fields(texts)
        image = ocr.crop_lines(image, [position])[0]
        show([image], title=str(texts))

    else:
        texts = lst_text[pos_start:pos_end+1]
        texts = check_fields(texts)
        return texts