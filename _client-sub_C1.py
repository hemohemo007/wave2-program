#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import redis
import glob

#broker_address = "127.0.0.1"
broker_address = "test.mosquitto.org"
#RedisHost = "127.0.0.1"
Topic = "C1_to_C2"

#files = glob.glob("./PMAX/*")
#or file in files:
#    print(file)
#   str=files

#r = redis.Redis(host=RedisHost, port='6379',db=0)
#
#r = redis.Redis(host="redis-14787.c82.us-east-1-2.ec2.cloud.redislabs.com", port="14787", db=0,password="50T5RWVcwdpQrFXkq26rTxgQwc7Ru1c7")
#

def on_message(client, userdata, message):
    m = str(message.payload.decode("utf-8"))
    print("message received " + m)
#
#
#    files = glob.glob("./PMAX/*")
#    for file in files:
#        print(file)
#        print(file[21:33])
#       print(file[16:20])
#        r.sadd(file[21:33], file[16:20])
#

#       r.sadd('KEY-h2', 'dateB', 'dataC', 'data6')
#       r.sadd('KEY-h3', 'date11', 'data8', 'data999')
#    r.set('RPIvalue',m)
#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)


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
