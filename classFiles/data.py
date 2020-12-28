from sense_hat import SenseHat
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

sense = SenseHat()

class Data():
    def __init__(self, config, logger):
        self.server = config['bridge']['ip']
        self.port = config['bridge']['port']
        self.logger = logger

    def getTemp(self):
        return sense.get_temperature()

    def getPres(self):
        return sense.get_pressure()

    def getHumid(self):
        return sense.get_humidity()

    def getCurrentReading(self, sensor):
        if sensor == 'temperature':
            return sense.get_temperature()
        elif sensor == 'pressure':
            return sense.get_pressure()
        elif sensor == 'humidity':
            return sense.get_humidity()
        else:
            return f'That sensor does not exist'