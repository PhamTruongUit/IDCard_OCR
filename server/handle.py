from src import libs
from src.ocr import ocr_custom
from src.libs.read_show_data import read, show
from PIL import Image
import os
import gdown
from pyvi import ViUtils

OPTIONS = {
        "01": "blur_bilateral",
        "02": "inc_brightness",
        "03": "dec_brightness",
        "04": "inc_contract",
        "05": "dec_contract",
        "06": "Erosion",
        "07": "Dilation",
        "08": "Opening",
        "09": "Closing",
        "10": "histogram",
        "11": "auto_rotation",
        "12": "detect_object"
    }

def image_preprocess(image, lst=[]):

    if lst:
        if lst[0] == 'none':
            None      
        elif lst[0] == 'auto':
            image = getattr(libs, "auto_rotation")(image)
            image = getattr(libs, "detect_object")(image)
        else:
            # image processing
            for attr in lst:
                opt = OPTIONS[attr]
                # print(opt)
                # call function libs.attribute()
                try:
                    image = getattr(libs, opt)(image)
                except:
                    None
    return image

def image_process(image="", path="", lst=[]):
    if not image:
        try:
            image = read(path)
        except: 
            raise ValueError(f'{path} does not exist')
    # pre processing
    image_result = image_preprocess(image, lst)
    # call model
    obj = ocr_custom(image = image_result)
    text = obj["text"]
    
    return image, text

def url_process(url_drive):
    temp_path = "temp"
    result_path = "results"

    # remove last result
    clear_file (temp_path)
    clear_file (result_path)
    
    json_data = {}    
    gdown.download_folder(url_drive, output = temp_path, remaining_ok=True)
    list_files = os.listdir(temp_path)  

    lst_tail = ['jpg','jpeg','png']

    for id in range(len(list_files)):
        file = list_files[id]
        name = file.split('.')[0]
        tail = file.split('.')[1]
        
        if tail not in lst_tail:
            continue

        # auto rename files 
        new_name = ViUtils.remove_accents(name).decode("utf-8") 
        old_file = os.path.join(temp_path,f'{name}.{tail}')
        new_file = os.path.join(temp_path,f'{new_name}.{tail}')
        os.rename(old_file, new_file)
        name = new_name

        file_path = os.path.join(temp_path,f'{name}.{tail}')
        # print(file_path)
        obj = ocr_custom(path=file_path)
        image = obj["img"]
        text = obj["text"]

        save_path = os.path.join(result_path, f'{name}.{tail}')   
        Image.fromarray(image).save(save_path)
        abs_path = os.path.abspath(save_path)

        # create json
        json_data[f'{id}'] = []
        json_data[f'{id}'].append({
            "img": f'{abs_path}',
            "text": text
        })
    
    # remove temp
    clear_file (temp_path)

    return json_data

def clear_file(path):
    for f in os.listdir(path):
        if f != "__init__.py":
            os.remove(os.path.join(path, f))

if __name__ == "__main__":
    # clear_file("./result")
    # image_process(path = "./src/images/01.jpg", lst=["12"])
    # url_process(0)
    None