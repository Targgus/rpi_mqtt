import json

rpi_broker = {
    'ip': 'localhost',
    'port' : 1833,
    'keepalive' : 60
}

def getConfig(str):
    if str == 'rpi_broker':
        return json.loads(json.dumps(rpi_broker))