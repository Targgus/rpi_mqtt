import logging
from logging.handlers import RotatingFileHandler

# Function to set up the logging. In this setup it will write to the screen
# and to a file at the same time

def setUpLogging():
  # create logger
  logger = logging.getLogger('mqtt.client') 
  logger.setLevel(logging.INFO)

  # Create the formatter
  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

  # create console handler and set level to debug
  ch = logging.StreamHandler()
  ch.setLevel(logging.DEBUG)
  ch.setFormatter(formatter)
  # Add the handlers to the logger
  logger.addHandler(ch)

  # Add a file handeler
  # fh = RotatingFileHandler('C:\\Users\\jlhen\\OneDrive\\Python\\OVV\\mqtt_critical_rate\\logs\\mqtt_client.log',maxBytes=50000, backupCount=10)
  # fh.setLevel(logging.DEBUG)
  # fh.setFormatter(formatter)
  # logger.addHandler(fh)

  return(logger)