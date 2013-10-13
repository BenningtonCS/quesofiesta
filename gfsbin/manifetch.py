#!/usr/bin/env python

#########################################################################
#									#
#	manifetch.py securely copies the manifest from the master	#
#	server to the client						#
#									#
#########################################################################


import os

# Get the master server address from the HOSTS config file
with open("HOSTS.config", "r") as hostfile:
	# Seperate each line at the equals sign, creating an array with [0] being the descriptor and [1] being the address
	HOST = hostfile.readline().split("=")
	# Store the value of the host address, stripping off the newline character at the end
	HOST = HOST[1].strip()

# Securely copy the manifest from the master server to the /data/temp directory on the raspberry pi client
os.system("scp " + HOST + ":/data/gfsbin/manifest.txt /data/temp/manifest.txt")
