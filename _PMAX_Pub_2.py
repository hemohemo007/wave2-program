#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import redis
import glob
import subprocess

#broker_address = "127.0.0.1"
broker_address = "test.mosquitto.org"
#RedisHost = "127.0.0.1"
Topic = "C1_to_C2"
Msg = "OOOOOOOO"


bin = input("BIN file name : ")
cmd= 'pmax.bat ' + str(bin)
print(cmd)

res = subprocess.Popen(cmd)
print(res)

f=open("SRP_1.data", "r")
srp=f.read()
print(srp)
f.close()


#
#

# publish MQTT
print("creating new instance")
client = mqtt.Client("pub2") #create new instance

print("connecting to broker: %s" % broker_address)
client.connect(broker_address) #connect to broker

files = glob.glob("./PMAX/*")

for file in files:
    print(file)
    print(file[21:33])
    print(file[16:20])
    val = file[16:20] + "   " + srp
    print("Publishing message: %s to topic: %s" % (val, Topic))
    client.publish(Topic,val)
#    r.sadd(file[21:33], val)


#       r.sadd('KEY-h2', 'dateB', 'dataC', 'data6')
#       r.sadd('KEY-h3', 'date11', 'data8', 'data999')
#    r.set('RPIvalue',m)
#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)






