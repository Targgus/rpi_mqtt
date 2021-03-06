import paho.mqtt.client as mqtt
import json

from Broker import brokerConfig as brokerConfig
from Message.Message import *
from Broker.Broker import *
from Data.Data import *

class Sender():
    def __init__(self, rpi_sensor):
        self.rpi_sensor = rpi_sensor

    def returnJsonObj(self, obj):
        return json.loads(json.dumps(obj))

    def initialize(self):
        self.senderConfig = self.returnJsonObj(self.rpi_sensor)
        self.brokerConfig = brokerConfig.getConfig(self.senderConfig['mqtt_broker'])

    def send(self):
        data = Data()
        message = MQTTMessage(self.senderConfig['topic'], data.returnData(self.senderConfig['sensor']))
        broker = MQTTSender(self.brokerConfig)
        broker.connect()
        broker.sendMessages(message)
        broker.disconnect()

