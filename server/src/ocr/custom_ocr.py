import src.ocr as ocr
import easyocr
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import matplotlib.pyplot as plt
# from src.setting.config import config
from numpy import argmax
from src.libs.read_show_data import read

#Custom fields
TEMPLATE = [
    # cmnd
    ["tên", "ĐKHK", "Sinh ngày", "Nguyên quán"],
    # cccd
    ["tên", "Nơi thường trú", "Ngày", "Giới tính", "Quê quán"],
]

def lst_show(lst_lines, names, title="", figsize=(16, 10)):
    l = len(lst_lines)
    fig = plt.figure(num = "Result", figsize=figsize)
    fig.suptitle(title, fontsize=16)
    for i in range(0, l):
        img = lst_lines[i]
        fig.add_subplot(l, 1, i+1)
        if names:
            plt.title(names[i])
        plt.imshow(img)
    plt.show()

def fit_fields(lst_text="", TEMPLATE="", index_start=0):
    temp = ocr.format_text(lst_text)
    template = ocr.format_fields(TEMPLATE)
    lst_count = [0]*len(template)
    default_count = [0]*len(template)
    flag_param = [0]*len(template)
    flag_start = 0
    flag_end = 0
    for id_temp in range(len(template)):
        fields = template[id_temp]       
        # get flag_start and flag_end of template about one obj
        for i in range(index_start, len(temp)):
            if ocr.search_custom(temp[i], [fields[0]]):
                flag_start = i
                break   

        for i in range(index_start+1, len(temp)):
            if ocr.search_custom(temp[i], [fields[1]]):
                flag_end = i
                break 

        # print(flag_start, flag_end)
        # print(id_temp)
        # print('---------------------')

        if flag_start >= flag_end: 
            continue 
        
        # print(flag_start, flag_end)
        # print(id_temp)
        # print('---------------------')

        flag_param[id_temp] = [flag_start,flag_end]
        # get template similar 
        default_count[id_temp] = len(fields)
        while fields:
            check_field = fields.pop()
            for i in range(flag_start, flag_end+1):
                if ocr.search_custom(temp[i], [check_field]):
                    lst_count[id_temp] += 1
                    break
    
    # Calculate similar
    # print(lst_count)
    # print(default_count)

    for i in range(len(lst_count)):
        if lst_count[i] != 0:
            lst_count[i] = round(lst_count[i]/default_count[i], 4)

    id = argmax(lst_count) 

    # exception
    flag_param[id][1] += 1

    # print(id, flag_param[id])

    return id, flag_param[id]

def ocr_custom(image="", path="", save_img=False ,debug=False):
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

    if not image:
        image = read(path)  

    bounds = reader.readtext(image, flag = True)
    box = ocr.boxes_line(bounds)
    lst_lines = ocr.crop_lines(image, box)
    lst_text = ocr.OCR(lst_lines, detector)

    # print(lst_text)
    # fit_fields(lst_text, TEMPLATE)
    # get index_line
    try:
        id, flag_param = fit_fields(lst_text, TEMPLATE)
        pos_start = flag_param[0]
        pos_end = flag_param[1]
        # print(pos_start, pos_end, id)

        #crop image
        box_temp = box[pos_start:pos_end+1]
        position = ocr.cluster_paragraph(box_temp)
        image_crop = ocr.crop_lines(image, [position])[0]
        text_result = lst_text[pos_start:pos_end+1]
        print(f"_SUCCESS_ file in the directory: {path}")
    except:
        image_crop = "Fail"
        text_result = "Fail"
        print(f"_FAIL_ file in the directory: {path}")
        
    if debug:
        lst_show([image_crop], [f'id template: {id}'] )
    else:
        if save_img:
            return {
                "text": text_result
            }
        else:
            return {
                "img": image_crop,
                "text": text_result
            }