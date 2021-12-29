from pyvi import ViUtils
import numpy as np
from enchant.utils import levenshtein
from scipy.spatial.distance import cdist

def cluster_paragraph(lst_box_lines):
    # defaul value position
    y1, y2, x1, x2  = lst_box_lines[0]

    for value in lst_box_lines:
        y1 = value[0] if value[0] < y1 else y1 
        y2 = value[1] if value[1] > y2 else y2 
        x1 = value[2] if value[2] < x1 else x1
        x2 = value[3] if value[3] > x2 else x2
    return y1, y2, x1, x2 

def format_text(lst_text):
    lst_upper = []
    for text in lst_text:
        temp = text.upper()
        temp = ViUtils.remove_accents(temp)
        temp = temp.decode('utf-8')
        lst_upper.append(temp)
    return lst_upper

def format_fields(lst_fields):
    fm_fields = []
    for i in lst_fields:
        fm_fields.append(format_text(i))
    return fm_fields

def search_custom(text, lst_keys):
    for key in lst_keys:
        try:
            text.index(key)
            return True
        except:
            None
    return False

def get_all_minimum_id(lst):
    lst_id_result = []
    min_value = min(lst)
    for i in range(len(lst)):
        if lst[i] == min_value:
            lst_id_result.append(i) 
    return lst_id_result

def get_all_maximum_id(lst):
    lst_id_result = []
    max_value = max(lst)
    for i in range(len(lst)):
        if lst[i] == max_value:
            lst_id_result.append(i) 
    return lst_id_result

def get_index_flag(obj_levenshtein):
    obj_min_lev = []
    lst_distance_score = []
    score = np.array([0,0])[np.newaxis, :]

    for id in range(len(obj_levenshtein)):
        cal_distance = np.array(obj_levenshtein[id][1])[np.newaxis, :]
        eucli = cdist(cal_distance, score, metric='euclidean')[0]

        lst_distance_score.append(list(eucli))

    lst_id_template = get_all_minimum_id(lst_distance_score)

    for id in lst_id_template:
        obj_min_lev.append(obj_levenshtein[id][0])

    return obj_min_lev

def search_flag(lst_text, fields, index_start):
    obj_levenshtein = []
    # obj_levenshtein [                                   #id
    #                   [
    #                       [id, start, end]                      #[id][0]
    #                       [distance_start, distance_end]        #[id][1]        
    #                   ]                  
    #                 ]

    lst_distance_start = []
    lst_distance_end = []

    for id in range(len(fields)):

        field_start = fields[id][0]
        field_end = fields[id][1]
        # print(field)
        l_start = len(field_start)
        l_end = len(field_end)

        for j in range(len(lst_text)):
            text_start = lst_text[j][:l_start]
            text_end = lst_text[j][:l_end]

            distance_start = levenshtein(text_start, field_start)
            distance_end = levenshtein(text_end, field_end)

            lst_distance_start.append(distance_start)
            lst_distance_end.append(distance_end)

        lst_flag_start = get_all_minimum_id(lst_distance_start)
        lst_flag_end = get_all_minimum_id(lst_distance_end)
        try:
            if len(lst_flag_start) >= 2 or len(lst_flag_end) >= 2:
                for start in lst_flag_start:
                    if start > index_start:
                        flag_start = start
                        break
                for end in lst_flag_end:
                    if end > flag_start:
                        flag_end = end
                        break
            else:
                flag_start = lst_flag_start[0]
                flag_end = lst_flag_end[0]
            
            if flag_start >= flag_end:
                obj_levenshtein.append([[id, -1, -1], [len(text_start), len(text_end)]])  
            
            else:
                obj_levenshtein.append([[id, flag_start, flag_end],
                                    [lst_distance_start[flag_start], lst_distance_end[flag_end]]])
        except:
            obj_levenshtein.append([[id, -1, -1], [len(text_start), len(text_end)]])     
        
        lst_distance_start.clear()
        lst_distance_end.clear()
    # print(obj_levenshtein)
    return obj_levenshtein

if __name__ == '__main__':
    # obj_fail = [ [[-1, -1], [5, 8]],[[20, 31], [0, 0]] ]
    # obj = [ [[9, 17], [0, 0]], [[20, 31], [0, 0]] ]
    # get_index_flag(obj)
    None
    