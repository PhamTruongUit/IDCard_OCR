import src.ocr as ocr
import easyocr
from vietocr.tool.predictor import Predictor
from vietocr.tool.config import Cfg
import matplotlib.pyplot as plt
from src.setting.config import config
from numpy import argmax
from src.libs.read_show_data import read, show

TEMPLATES = config.TEMPLATES

def fit_fields(lst_text, index_start=0):
    temp = ocr.format_text(lst_text)
    templates = ocr.format_fields(TEMPLATES)
    lst_count = [0]*len(templates)
    default_count = [0]*len(templates)
    flag_param = [0]*len(templates)
    flag_start = 0
    flag_end = 0
    for id_temp in range(len(templates)):
        fields = templates[id_temp]       
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

    # check exception
    try:
        flag_param[id][1] += 1
    except:
        None

    # print(id)
    # print(flag_param[id])

    return id, flag_param[id]

def fit_fields_v2(lst_text, index_start=0):
    temp = ocr.format_text(lst_text)
    templates = ocr.format_fields(TEMPLATES)
    lst_count = [0]*len(templates)
    default_count = [0]*len(templates)
    flag_param = [0]*len(templates)
    obj_levenshtein = ocr.search_flag(temp, templates, index_start)
    obj_min_lev = ocr.get_index_flag(obj_levenshtein)

    # print(obj_levenshtein)
    # print(obj_min_lev)
    
    for id_temp, flag_start, flag_end in obj_min_lev:

        fields = templates[id_temp]       

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

    if index_start == 0: 
        for i in range(len(lst_count)):
            if i % 2 == 0:
                lst_count[i] = 0
    else:
        for i in range(len(lst_count)):
            if i % 2 == 1:
                lst_count[i] = 0
   
    lst_id = ocr.get_all_maximum_id(lst_count)
    # print(lst_id)
    if len(lst_id) >= 2: 
        fit_id = lst_id[0]
        
        for id in lst_id:
            if default_count[id] > default_count[fit_id]:
                    fit_id = id

        # check exception
        if fit_id == 8:
            flag_param[fit_id][1] -= 1
    
    else:
        fit_id = lst_id[0]

    try:
        flag_param[fit_id][1] += 1
    except:
        None
    # print(fit_id, flag_param[fit_id])
    return fit_id, flag_param[fit_id]

def check_index_fail(flag_param):
    if flag_param == 0:
        return False

    if len(flag_param) == 2:
        if flag_param[0] <= 0 or flag_param[1] <= 0: 
            return False
        if flag_param[0] >= flag_param[1]: 
            return False

    return True

def ocr_custom(detector, reader, image=None, path="", save_img=False ,debug=False):

    if path:
        image = read(path)  

    try:
        bounds = reader.readtext(image, flag = True)
        box = ocr.boxes_line(bounds)
        lst_lines = ocr.crop_lines(image, box)
        lst_text = ocr.OCR(lst_lines, detector)

        # print(lst_text)
        # fit_fields(lst_text, TEMPLATES)
        # get index_line

        id, flag_param = fit_fields(lst_text)
        if not check_index_fail(flag_param):
            id, flag_param = fit_fields_v2(lst_text)

        pos_start = flag_param[0]
        pos_end = flag_param[1]
        # print(pos_start, pos_end, id)

        #crop image
        box_temp = box[pos_start:pos_end+1]
        position = ocr.cluster_paragraph(box_temp)
        image_crop = ocr.crop_lines(image, [position])[0]
        text_result = lst_text[pos_start:pos_end+1]

        if path:
            print(f"_SUCCESS_ file in the directory: {path}")
        else:
            print(f"_SUCCESS_ image")
    except:
        image_crop = "None"
        text_result = "None"
        if path:
            print(f"_FAIL_ file in the directory: {path}")
        else:
            print(f"_FAIL_ image")
        
    if debug:
        if id == 0:
            type_template = "CMND"
        else:
            type_template = "CCCD"
        show([image_crop], [f'Type: {type_template}'] )
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