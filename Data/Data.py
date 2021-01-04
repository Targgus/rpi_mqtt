from sense_hat import SenseHat
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import json

sense = SenseHat()

class Data():
    def __init__(self):
        pass

    def returnData(self, sensor):
        if sensor == 'temperature':
            body = {"temperature" : sense.get_temperature()}
            return json.dumps(body)
        elif sensor == 'pressure':
            body = {"pressure" : sense.get_pressure()}
            return json.dumps(body)
        elif sensor == 'humidity':
            body = {"humidity" : sense.get_humidity()}
            return json.dumps(body)
        elif sensor == 'all':
            body = {
                "temperature" : sense.get_temperature(),
                "pressure" : sense.get_pressure(),
                "humidity" : sense.get_humidity()
            }
            return json.dumps(body)
        else:
            return f'That sensor does not exist'    