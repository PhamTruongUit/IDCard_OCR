from src import libs
from src.ocr import ocr_custom
from src.libs.read_show_data import read
from PIL import Image
import os
import gdown
from pyvi import ViUtils
import time
from src.setting.config import config
import logging
from datetime import datetime

def get_option(lst_encode):
    lst_decode = []
    OPTIONS = config.OPTIONS
    for attr in lst_encode:
        opt = OPTIONS[attr]
        lst_decode.append(opt)
    return lst_decode

def preprocess(image, lst=[]):
    if lst:
        if lst[0] == 'none':
            None      
        elif lst[0] == 'auto':
            image = getattr(libs, "auto_rotation")(image)
            image = getattr(libs, "auto_detect")(image)
        else:
            # image processing
            for attr in lst:
                try:
                    image = getattr(libs, attr)(image)
                except:
                    None
    return image

def image_process(detector, reader, image=None, path="", lst_encode=[]):
    if path:
        try:
            image = read(path)
        except: 
            raise ValueError(f'{path} does not exist')

    lst_decode = get_option(lst_encode)
    print(lst_decode)
    # pre processing
    start_process = time.time()
    image_result = preprocess(image, lst_decode)
    end_process = time.time()

    # # call model
    start_ocr = time.time()
    obj = ocr_custom(detector=detector, reader=reader, image = image_result)
    text = obj["text"]
    end_ocr = time.time()

    #logger
    handlers = [logging.FileHandler('./logs/request.log', 'a', 'utf-8')]
    logging.basicConfig(handlers=handlers, level=logging.DEBUG)
    logging.info(f'Datetime: {datetime.now()}')
    logging.info(f'List Option: {lst_decode}')
    logging.info(f'Time preprocess image: {round(end_process-start_process, 4)}')
    logging.info(f'Time recognize text: {round(end_ocr-start_ocr, 4)}')
    
    return image_result, text

def path_process(detector, reader, path="temp"):
    json_data = {} 
    result_path = "results"

    clear_file(result_path)
    
    list_files = os.listdir(path)  

    lst_tail = ['jpg','jpeg','png']

    handlers = [logging.FileHandler('./logs/debug.log', 'w', 'utf-8')]
    logging.basicConfig(handlers=handlers, level=logging.DEBUG)
    time_average = []
    for id in range(len(list_files)):
        file = list_files[id]
        name = file.split('.')[0]
        tail = file.split('.')[1]
        
        if tail not in lst_tail:
            continue

        # auto rename files 
        new_name = ViUtils.remove_accents(name).decode("utf-8") 
        old_file = os.path.join(path,f'{name}.{tail}')
        new_file = os.path.join(path,f'{new_name}.{tail}')
        os.rename(old_file, new_file)
        name = new_name

        file_path = os.path.join(path,f'{name}.{tail}')
        # print(file_path)
        start_ocr = time.time()
        obj = ocr_custom(detector=detector, reader=reader, path=file_path)
        end_ocr = time.time()
        image = obj["img"]
        text = obj["text"]

        save_image_path = os.path.join(result_path, f'{name}.{tail}')   
        save_text_path = os.path.join(result_path, f'{name}.txt')  

        Image.fromarray(image).save(save_image_path)

        abs_path = os.path.abspath(save_image_path)
        t = round(end_ocr-start_ocr, 4)
        logging.info(f'Datetime: {datetime.now()}')
        logging.info(f'Time recognize text: {t}')
        logging.info(f'Img: {abs_path}')
        logging.info(f'Text:')
        for te in text:
            logging.info(f'     {te}')
        
        time_average.append(t)

        # create json
        json_data[f'{id}'] = []
        json_data[f'{id}'].append({
            "img": f'{abs_path}',
            "text": text
        })
    t_average = sum(time_average)/len(time_average)
    logging.info(f'Time average: {t_average}')

    return json_data

def url_process(detector, reader, url_drive):
    temp_path = "temp"
    result_path = "results"

    # remove last result
    clear_file (temp_path)
    clear_file (result_path)
    
    json_data = {}    
    gdown.download_folder(url_drive, output = temp_path, remaining_ok=True)
    list_files = os.listdir(temp_path)  

    lst_tail = ['jpg','jpeg','png']

    handlers = [logging.FileHandler('./logs/debug.log', 'w', 'utf-8')]
    logging.basicConfig(handlers=handlers, level=logging.DEBUG)
    time_average = []
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
        start_ocr = time.time()
        obj = ocr_custom(detector=detector, reader=reader, path=file_path)
        end_ocr = time.time()
        image = obj["img"]
        text = obj["text"]

        save_image_path = os.path.join(result_path, f'{name}.{tail}')   
        save_text_path = os.path.join(result_path, f'{name}.txt')   

        Image.fromarray(image).save(save_image_path)

        abs_path = os.path.abspath(save_image_path)
        t = round(end_ocr-start_ocr, 4)
        logging.info(f'Datetime: {datetime.now()}')
        logging.info(f'Time recognize text: {t}')
        logging.info(f'Img: {abs_path}')
        logging.info(f'Text:')
        for te in text:
            logging.info(f'     {te}')

        time_average.append(t)

        # create json
        json_data[f'{id}'] = []
        json_data[f'{id}'].append({
            "img": f'{abs_path}',
            "text": text
        })
    t_average = sum(time_average)/len(time_average)
    logging.info(f'Time average: {t_average}')
    
    # remove temp
    clear_file (temp_path)

    return json_data

def clear_file(path):
    for f in os.listdir(path):
        if f != "__init__.py":
            os.remove(os.path.join(path, f))

if __name__ == "__main__":
    # from src.ocr.models import load_model
    # detector, reader = load_model()
    # image_process(detector = detector, reader = reader, path = "./src/images/02.jpg", lst=["none"])
    # path_process(detector = detector, reader = reader, path = "./src/images")
    None