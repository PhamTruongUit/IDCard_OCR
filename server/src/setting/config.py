import ast
from configparser import ConfigParser

config = ConfigParser()
config.read("../config.ini")
config.PORT = config.get("server", "port")
config.HOST = config.get("hosting","address")
