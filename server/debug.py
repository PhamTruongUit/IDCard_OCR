import time
import sys
from src.ocr import ocr_custom
from src.ocr.models import load_model 

if __name__ == '__main__':
    detector, reader = load_model()
    # print(config.OPTIONS['01'])
    if len(sys.argv) < 2: 
        # print(len(sys.argv))
        print('please input \'python debug.py %pathfile\'')
    else:
        path = sys.argv[1]
        try:
            start_time = time.time()
        except Exception:
            print('path error, please try again')
        ocr_custom(detector=detector, reader=reader, path = path, debug=True)
        print(f"--- {round(time.time() - start_time, 4)} seconds ---")