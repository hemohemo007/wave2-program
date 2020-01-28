#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import redis
import glob
import subprocess

bin = input("BIN file name : ")
cmd= 'pmax.bat ' + str(bin)
print(cmd)
input()

res = subprocess.Popen(cmd)
print(res)

f=open("SRP_1.data", "r")
s=f.read()
print(s)
f.close()

