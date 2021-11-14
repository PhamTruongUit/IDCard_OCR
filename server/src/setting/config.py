from configparser import ConfigParser as cfg

config = cfg()
config.read("../config.ini", encoding="utf8")
config.PORT = config.get("server", "port")
config.HOST = config.get("hosting","address")

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