from classFiles.data import Data

class Message(Data):
    def __init__(self, config, logger, sensor):
        self.data = Data(config, logger)
        self.sensor = sensor
        self.hostname = config['bridge']['ip']
        self.port = config['bridge']['port']
        self.client_id = config['bridge']['client_id']
        self.keepalive = config['bridge']['keepalive']

    def createTopic(self):
        return f'rpi/sensor/{self.sensor}'

    def createBody(self):
        return data.getCurrentReading(self.sensor)

    def publishMessage(self):
        publish.single(
            self.createTopic(),
            self.createBody(),
            0,
            False,
            hostname = self.hostname,
            port = int(self.port),
            client_id = self.client_id,
            keepalive = int(self.keepalive)
        )

