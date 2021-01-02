import json

rpi_temp_sender = {
    'topic' : 'rpi/sensor/temp',
    'mqtt_broker': 'rpi_broker'
}

def getConfig(str):
    if str == 'rpi_temp_sender':
        print(str)
        return json.loads(json.dumps(rpi_temp_sender))
        