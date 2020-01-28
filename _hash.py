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

#r = redis.Redis(host=RedisHost, port='6379',db=0)
#
r = redis.Redis(host="redis-14787.c82.us-east-1-2.ec2.cloud.redislabs.com", port="14787", db=0,password="50T5RWVcwdpQrFXkq26rTxgQwc7Ru1c7")
#

#res = subprocess.Popen('pmax.bat')
#print(res)

#f=open("SRP_1.data", "r")
#s=f.read()
#print(s)
#f.close()


#
#
#files = glob.glob("./PMAX/*")

#for file in files:
#    print(file)
#    print(file[21:33])
#    print(file[16:20])
#    r.sadd(file[21:33], file[16:20],s)

r.hset('KEY-h2', '0000', 'Taro')
r.hset('KEY-h2', '1111', 'Kei')
r.hset('KEY-h2', '2222', 'Mia')
r.hset('KEY-h2', '3333', 'Japan')
r.hset('KEY-h2', '4444', 'Jhon')

#       r.sadd('KEY-h3', 'date11', 'data8', 'data999')
#    r.set('RPIvalue',m)
#    print("message topic=",message.topic)
#    print("message qos=",message.qos)
#    print("message retain flag=",message.retain)

# publish MQTT
print("creating new instance")
client = mqtt.Client("pub2") #create new instance

print("connecting to broker: %s" % broker_address)
client.connect(broker_address) #connect to broker

print("Publishing message: %s to topic: %s" % (Msg, Topic))
client.publish(Topic,Msg)




