import ConfigParser
import appconfig

DATA_BASE_CONFIG = 'DATABASE'
REQ_HEADERS_MOZILLA = 'REQ_HEADERS_MOZILLA'
URL = 'URL'
IMAGE_PATH = 'IMAGE_PATH'

config = ConfigParser.ConfigParser()
config.read("appconfig.cfg")

def get_config(key):
    app_config_dict = {}
    options = config.options(key)
    for option in options:
        app_config_dict[option] = config.get(key, option)
    return app_config_dict



