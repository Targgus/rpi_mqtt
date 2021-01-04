import json

rpi_temp_sender = {
    'topic' : 'rpi/sensor/temp',
    'mqtt_broker': 'rpi_broker',
    'sensor' : 'temperature'
}

rpi_humidity_sender = {
    'topic' : 'rpi/sensor/humidity',
    'mqtt_broker': 'rpi_broker',
    'sensor' : 'humidity'
}

rpi_press_sender = {
    'topic' : 'rpi/sensor/press',
    'mqtt_broker': 'rpi_broker',
    'sensor' : 'presssure'
}

rpi_all_sender = {
    'topic' : 'rpi/sensor/all',
    'mqtt_broker': 'rpi_broker',
    'sensor' : 'all'
}

def getConfig(str):
    if str == 'rpi_temp_sender':
        print(str)
        return json.loads(json.dumps(rpi_temp_sender))
    elif str == 'rpi_humidity_sender':
        print(str)
        return json.loads(json.dumps(rpi_humidity_sender))
    elif str == 'rpi_pressure_sender':
        print(str)
        return json.loads(json.dumps(rpi_press_sender))
    elif str == 'rpi_all_sender':
        print(str)
        return json.loads(json.dumps(rpi_all_sender))
        