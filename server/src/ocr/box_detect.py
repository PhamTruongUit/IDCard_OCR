import numpy as np

def unique_list(lst):
    check = []
    return [x for x in lst if x not in check and not check.append(x)]

def cluster_lines(box_1, box_2):
    y1 = box_1[0] if box_1[0] < box_2[0] else box_2[0]
    y2 = box_1[1] if box_1[1] > box_2[1] else box_2[1] 
    x1 = box_1[2] if box_1[2] < box_2[2] else box_2[2]
    x2 = box_1[3] if box_1[3] > box_2[3] else box_2[3]
    return y1, y2, x1, x2 

def crop_lines(image, lst_box):
    lst_lines = []
    image = np.array(image)
    for y1,y2,x1,x2 in lst_box:
        crop_image = image[x1:x2, y1:y2, :].copy()
        lst_lines.append(crop_image)

    return lst_lines

def boxes_line(bounds=[], min=20):
    lst_box = []
    flag = bounds[0]
    mutil_box = False # flag for 1 box in 1 line
    for i in range(len(bounds)):
        if bounds[i][3] - flag[3] < min: # distance for top of 2 line 
            mutil_box = True
            position = cluster_lines(flag, bounds[i])
        else:
            if not mutil_box:
                position = flag
            else:
                mutil_box = False
            lst_box.append(position) 
            flag = bounds[i]
            
    #Last value
    if not mutil_box:
        position = flag  
    lst_box.append(position) 

    #Format list box 
    lst_box = unique_list(lst_box)
    return lst_box