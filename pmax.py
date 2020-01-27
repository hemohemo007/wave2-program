#!/usr/bin/env python3

import glob
import subprocess

files = glob.glob("PMAX/*")
for file in files:
    print(file)
    print(len(file))
    ppp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(file[19:31])
    print(file[14:18])
#    print(ppp[14:15])
#    print(ppp[9:4])
#
#
# HHHHH
#

res = subprocess.Popen('pmax.bat')
print(res)

f=open("SRP_1.data", "r")
s=f.read()
print(s)
f.close()




