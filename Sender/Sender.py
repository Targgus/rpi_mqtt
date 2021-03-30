import paho.mqtt.client as mqtt
import json

import senderConfig as sc

from Broker import brokerConfig as brokerConfig
from Message.Message import *
from Broker.Broker import *
from Data.Data import *

class Sender():
    def __init__(self):
        # get broker ip, port, and keepalive from sub class
        self.brokerConfig = brokerConfig.getConfig(self.broker_config)
        # instantiate broker with ip, port, and keepalive info
        self.broker = MQTTSender(self.brokerConfig)
        # establish connection to broker
        self.broker.connect()

        self.data = Data()

    def getData(self, sensor):
        return self.data.returnRawData(sensor)

class genericSender():
    pass

class tempSender(Sender):
    def __init__(self):
        
        self.config = sc.getConfig('rpi_temp_sender')
        self.broker_config = self.config['mqtt_broker']
        self.sensor = self.config['sensor']
        self.topic = self.config['topic']

        super().__init__()
        self.data = Data()

    # def getTemp(self):
    #     return self.data.returnRawData(self.sensor)

    def sendTemp(self):
        # create mqtt message
        message = MQTTMessage(self.topic)
        message.setBody(self.sensor, self.getData(self.sensor))

        # use client from connected broker to send message
        self.broker.client.publish(message.topic, str(message.body))

