import configparser
from classFiles.message import Message
from classFiles.mqtt_logger import setUpLogging

logger = setUpLogging()

config = configparser.ConfigParser()
config.read('config.ini')

temp_message = Message(config, logger, 'temperature')

