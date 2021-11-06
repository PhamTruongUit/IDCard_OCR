import ast
from configparser import ConfigParser

config = ConfigParser()
config.read("../config.ini")
config.API_KEY = config.get("api", "key")
config.LANGUAGE = config.get("api","language")
config.PORT_SERVER = config.get("server", "port")
config.PORT_CLIENT = config.get("client", "port")
config.HOST = config.get("hosting","address")
config.START = ast.literal_eval(config.get("ocr","starts"))
config.END = ast.literal_eval(config.get("ocr","ends"))
config.FIELDS = ast.literal_eval(config.get("ocr","fields"))