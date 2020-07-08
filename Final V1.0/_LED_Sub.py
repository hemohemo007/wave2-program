#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
####import redis
####import glob
import RPi.GPIO as GPIO
#import ds18b20
import i2c_lcd1602


#broker_address = "127.0.0.1"
broker_address = "test.mosquitto.org"
#RedisHost = "127.0.0.1"
Topic = "C1_to_C2"

screen = i2c_lcd1602.Screen(bus=1, addr=0x27, cols=16, rows=2)
line = "PowerMax SRP_1"

def on_message(client, userdata, message):
    m = str(message.payload.decode("utf-8"))
    print("message received " + m)
    srp = m.split()
    print("=== Usable Capacity === Total : " + srp[10] + " TB  / Used : " + srp[11] + " %  " )
    if int(srp[11]) > 70:
        han = "NG"
    else:
        han = "OK"
    screen.cursorTo(0, 0)
    screen.println(line)
    screen.cursorTo(1, 0)
    screen.println('Used : ' + srp[11] + ' % ' + han)
    screen.clear()


screen.enable_backlight()
screen.clear()

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
