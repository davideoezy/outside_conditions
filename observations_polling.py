

import urllib.request
import json
import datetime
import time
import paho.mqtt.client as mqtt

# Set variables
topic = "sensors/outside/observations"
measurement = "temperature"
location = "outside"

# BOM readings
url = 'http://reg.bom.gov.au/fwo/IDV60901/IDV60901.94870.json'

# Broker details:
broker_address="192.168.0.10" 
client = mqtt.Client("P1")
client.connect(broker_address)

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

    reading_influx = "%s,location=%s air_temp=%s,apparent_t=%s,reading_age=%s" % (measurement, location, air_temp, apparent_t, reading_age)
    print(reading_influx)

    client.publish(topic,str(reading_influx))
    time.sleep(600)
