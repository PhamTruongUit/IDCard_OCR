from configparser import ConfigParser

config = ConfigParser()
config.read("../config.ini")
config.API_KEY = config.get("api", "key")
config.LANGUAGE = config.get("api","language")
config.SERVER = config.get("server", "port")
config.CLIENT = config.get("client", "port")