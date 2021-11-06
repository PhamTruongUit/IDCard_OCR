import time
import cv2
import sys
import src.tools as tools
from src.setting.config import config
from src.libs.threshold import threshold
from src.ocr import ocr_custom
from src.libs.read_show_data import read

if __name__ == '__main__':

    file_name = '02.jpg'
    path = f'./src/images/{file_name}' 

    if len(sys.argv) < 2: 
        # print(len(sys.argv))
        print('please input \'python debug.py %pathfile\'')
    else:
        path = sys.argv[1]
        try:
            image = read(path)
            start_time = time.time()
        except Exception:
            print('path error, please try again')
        print(ocr_custom(image, debug=False))
        print("--- %s seconds ---" % (time.time() - start_time))