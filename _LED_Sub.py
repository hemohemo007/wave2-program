#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import redis
import glob

#broker_address = "127.0.0.1"
broker_address = "test.mosquitto.org"
#RedisHost = "127.0.0.1"
Topic = "C1_to_C2"


def on_message(client, userdata, message):
    m = str(message.payload.decode("utf-8"))
    print("message received " + m)


print("creating new instance")
client = mqtt.Client() #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker

client.loop_start() #start the loop

while True:
    client.subscribe(Topic)
    time.sleep(2) # wait

client.loop_stop() #stop the loop
