from pyvi import ViUtils
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