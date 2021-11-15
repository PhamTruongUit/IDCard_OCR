import time
import sys
from src.ocr import ocr_custom
from src.ocr.models import load_model 
from src import libs
from src.libs.read_show_data import read, show

if __name__ == '__main__':
    # image = read("src/images/03.jpg")
    # result = libs.inc_brightness(image, 50)
    # result = libs.auto_rotation(image)
    # show([image, result])
    # detector, reader = load_model()
    # ocr_custom(detector=detector, reader=reader, image = image, debug=True)
    # ocr_custom(detector=detector, reader=reader, path = "src/images/03.jpg", debug=True)
    # if len(sys.argv) < 2: 
    #     # print(len(sys.argv))
    #     print('please input \'python debug.py %pathfile\'')
    # else:
    #     path = sys.argv[1]
    #     try:
    #         start_time = time.time()
    #     except Exception:
    #         print('path error, please try again')
    #     ocr_custom(detector=detector, reader=reader, path = path, debug=True)
    #     print(f"--- {round(time.time() - start_time, 4)} seconds ---")
    None