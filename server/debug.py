import src.libs as libs
import src.tools as tools 
from src.setting.config import config
from src.libs.threshold import threshold
from src.api.ocr import ocr_file  

API_KEY = config.API_KEY

file_name = '03.jpg'
path = f'./src/images/{file_name}' 

# mode attribute
# tools.rgbColor(path)
# tools.hsvColor(path)
# getattr(libs,'threshold')(path, 
#             mode='RGB', 
#             debug=True, 
#             low_color=[0,0,0], 
#             high_color=[255,255,255])

# mode module
# threshold(path, 
#             mode='RGB', 
#             debug=True, 
#             low_color=[0,0,0], 
#             high_color=[255,255,255])
print(ocr_file(path, api_key = API_KEY))
