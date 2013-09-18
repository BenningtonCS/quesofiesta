#! /usr/bin/env python

import os
import hashlib


GFS_PATH = "/data/gfsbin/"

if os.path.isfile(GFS_PATH + 'manifest.txt'):
        with open(GFS_PATH + 'manifest.txt', 'r') as f:
                VERSION_STR = f.readline()
		VERSION = int(VERSION_STR)
        os.remove(GFS_PATH + 'manifest.txt')

with open(GFS_PATH + "manifest.txt", "w") as a:
        NEW_VERSION = str(VERSION + 1)
        a.write(NEW_VERSION + os.linesep)
        for path, subdirs, files in os.walk(GFS_PATH):
                for filename in files:
                        f = os.path.join(path, filename)
                        if f != "/data/gfsbin/manifest.txt":
                                hex = hashlib.md5(open(str(f)).read()).hexdigest()
                                a.write(str(f) + "|" + hex + os.linesep)

with open(GFS_PATH + "manifest.txt", "r") as a:
        mhex = hashlib.md5(a.read()).hexdigest()

with open(GFS_PATH + "manifest.txt", "a") as a:
        a.write(GFS_PATH + "manifest.txt" + "|" + mhex + os.linesep)
