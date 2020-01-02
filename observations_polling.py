

import urllib.request
import json
import datetime
import time
import paho.mqtt.client as mqtt

# Set variables
topic = "home/outside/status"
measurementName = "temperature"
location = "outside"

# BOM readings
url = 'http://reg.bom.gov.au/fwo/IDV60901/IDV60901.94870.json'

# Broker details:
broker_address="192.168.0.10" 
client = mqtt.Client("docker_1")
client.connect(broker_address, keepalive=500)

def response(url):
    with urllib.request.urlopen(url) as response: 
        jsonString = response.read()
        jsonData = json.loads(jsonString.decode('utf-8'))
        current_reading = jsonData['observations']['data'][0]
    return(current_reading)

while True:

    locals().update(response(url))
    
    reading_ts = datetime.datetime.strptime(aifstime_utc, '%Y%m%d%H%M%S')
    reading_age = (datetime.datetime.utcnow() - reading_ts).seconds

    dict_msg={
        "measurement":measurementName, 
        "fields": {
            "air_temp":air_temp, 
            "apparent_t":apparent_t, 
            "reading_age":reading_age
            }, 
        "tags": {
            "location":location
            }
    }
    
    msg = json.dumps(dict_msg)

    print(msg)

    client.publish(topic,msg)
    time.sleep(10)
