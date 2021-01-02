import paho.mqtt.client as mqtt

class MQTTBroker():
    def __init__(self, brokerConfig):
        self.ip = brokerConfig['ip']
        self.port = brokerConfig['port']
        self.keepalive = brokerConfig['keepalive']
        print(f"{self.ip} {self.port} {self.keepalive}")


class MQTTSender(MQTTBroker):
    def __init__(self, brokerConfig):
        super().__init__(brokerConfig)

    def connect(self):
        self.client = mqtt.Client()
        self.client.connect(self.ip)

    def sendMessages(self, message):
        # for message in messages:
        self.client.publish(message.topic, str(message.body))

    def disconnect(self):
        self.client.disconnect()
