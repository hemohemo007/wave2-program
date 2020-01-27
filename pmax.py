#!/usr/bin/env python3

import glob

files = glob.glob("./PMAX/*")
for file in files:
    print(file)


