
import json
import requests
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


while True:
    response = None

    with requests.get(url, timeout = 30) as request:
        try:
            response = request.json()
            current_reading = response['observations']['data'][0]

            dict_msg={"location":location,
                "temperature":current_reading['air_temp'], 
                "feels_like":current_reading['apparent_t'],
                "humidity":current_reading['rel_hum']}

            msg = json.dumps(dict_msg)

            client.publish(topic,msg)

        except (requests.Timeout, requests.ConnectionError, requests.HTTPError) as err:
            print("Error while trying to GET data")
            print(err)

        finally:
            time.sleep(600)
