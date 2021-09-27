from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
config.API_KEY = config.get("api", "key")
config.LANGUAGES = config.get("api","languages")
config.SERVER = config.get("server", "port")
config.CLIENT = config.get("client", "port")
