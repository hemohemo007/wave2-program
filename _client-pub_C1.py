#!/usr/bin/env python3

import paho.mqtt.client as mqtt


###### Edit variables to your environment #######
broker_address = "test.mosquitto.org"     #MQTT broker_address
#broker_address = "127.0.0.1"     #MQTT broker_address
Topic = "C1_to_C2"
Msg = "Greetings from RPi !!!  Hello Pinky World"

# publish MQTT
print("creating new instance")
client = mqtt.Client("pub2") #create new instance

print("connecting to broker: %s" % broker_address)
client.connect(broker_address) #connect to broker

print("Publishing message: %s to topic: %s" % (Msg, Topic))
client.publish(Topic,Msg)

#################
## Alternatively you can send a single message without creating an instance
##print "sending now"
##mqtt.single(Topic, Msg, hostname=broker_address)
