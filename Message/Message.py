from Sender import *
import json

class MQTTMessage():

    def __init__(self, topic = None, body = None):
        self.topic = topic
        self.body = body

    def show(self):
        print(self.topic)
        print(self.body)

    def getBody(self):
        return self.body

    def getTopic(self):
        return self.topic

    def setBody(self, sensor, value):
        self.body = json.dumps({sensor : value})