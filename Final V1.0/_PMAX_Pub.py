#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import redis
import glob
import subprocess

#broker_address = "127.0.0.1"
#RedisHost = "127.0.0.1"
#r = redis.Redis(host=RedisHost, port='6379',db=0)

broker_address = "test.mosquitto.org"
Topic = "C1_to_C2"
Msg = "OOOOOOOO"

r = redis.Redis(host="redis-14787.c82.us-east-1-2.ec2.cloud.redislabs.com", port="14787", db=0,password="50T5RWVcwdpQrFXkq26rTxgQwc7Ru1c7")


# publish MQTT
print("creating new instance")
client = mqtt.Client("pub2") #create new instance

print("connecting to broker: %s" % broker_address)
client.connect(broker_address) #connect to broker

# Get PowerMax BIN filename & Pool information
# Redis SET data type
# publish MQTT to Pi _LED_Sub

files = glob.glob("./PMAX/*")

for file in files:
    print(file)
    print(file[7:37])
    bin = file[7:37]
    cmd= 'pmax.bat ' + str(bin)
    print(cmd)
    input()
    res = subprocess.Popen(cmd)
    print(res)
    f=open("SRP_1.data", "r")
    srp=f.read()
    print(srp)
    f.close()
    print(file[16:20])
    val = file[16:20] + "   " + srp
    print("Publishing message: %s to topic: %s" % (val, Topic))
    client.publish(Topic,val)
#    
    r.sadd(file[21:33], val)
#

#       r.sadd('KEY-h2', 'dateB', 'dataC', 'data6')
#       r.sadd('KEY-h3', 'date11', 'data8', 'data999')
#    r.set('RPIvalue',m)
#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)





