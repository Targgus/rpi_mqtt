from Sender import *

class MQTTMessage():

    def __init__(self, topic, body):
        self.topic = topic
        self.body = body

    def show(self):
        print(self.topic)
        print(self.body)

    def getBody(self):
        return self.body

    def getTopic(self):
        return self.topic


class Messages():
    def __init__(self):
        self.messages = []

    def appendMessages(self, msg, topic):
        
        message = MQTTMessage(topic, msg)
        self.messages.append(message)
        # for i in msg:
        #     # compose a message object with a topic and body
        #     message = MQTTMessage(topic, msg)
        #     self.messages.append(message)

    def returnMessages(self):
        return self.messages

    def showMessages(self):
        for message in self.messages:
            message.show()