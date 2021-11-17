from configparser import ConfigParser as cfg

config = cfg()
config.read("./config.ini", encoding="utf8")

config.HOST = config.get("hosting","address")
config.SERVER = config.get("server", "port")
config.CLIENT = config.get("client", "port")

device = config.get("models","device")
if device == "cuda":
    config.DEVICE = "cuda:0"
elif device == "cpu":
    config.DEVICE = "cpu"

weight = config.get("models","weight")
if weight == "drive":
    config.WEIGHT = "https://drive.google.com/uc?id=13327Y1tz1ohsm5YZMyXVMPIOjoOA0OaA"
elif weight == "local":
    config.WEIGHT = "./src/ocr/transformerocr.pth"


templates = dict(config.items('templates'))
config.TEMPLATES = []
for key in templates.keys():
    temp = templates[key]
    temp = temp.replace('[','')
    temp = temp.replace(']','')
    temp = temp.replace('\"','')
    temp = temp.replace('\'','')
    temp = temp.replace(', ',',')
    temp = temp.replace(' ,',',')
    temp = temp.split(',')
    config.TEMPLATES.append(temp)

config.OPTIONS = dict(config.items('options'))