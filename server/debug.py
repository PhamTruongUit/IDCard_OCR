import time
import sys
from src.ocr import ocr_custom
from src.libs.read_show_data import read

if __name__ == '__main__':
    if len(sys.argv) < 2: 
        # print(len(sys.argv))
        print('please input \'python debug.py %pathfile\'')
    else:
        path = sys.argv[1]
        try:
            start_time = time.time()
        except Exception:
            print('path error, please try again')
        print(ocr_custom(path, debug=False))
        print("--- %s seconds ---" % (time.time() - start_time))