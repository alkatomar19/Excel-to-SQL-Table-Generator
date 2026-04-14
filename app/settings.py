from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

SQL_CONFIG = config["sqlserver"]
PATHS = config["paths"]