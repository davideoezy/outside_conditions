

import urllib.request
import json
import datetime
import time
import paho.mqtt.client as mqtt

# Set variables
topic = "home/outside/sensor"
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

    try:
        locals().update(response(url))

        reading_ts = datetime.datetime.strptime(aifstime_utc, '%Y%m%d%H%M%S')
        reading_age = (datetime.datetime.utcnow() - reading_ts).seconds

        dict_msg={"location":location,"temperature":air_temp, "feels_like":apparent_t, "humidity":rel_hum}
        
        msg = json.dumps(dict_msg)

        client.publish(topic,msg)

    except:
        print("Error obtaining update")

    time.sleep(600)
