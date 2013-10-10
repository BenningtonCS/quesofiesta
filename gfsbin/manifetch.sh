#!/bin/sh


# Securely retrieve the master-hosted manifest and put it in the local /data/temp/ directory 
scp -r pi@10.10.100.144:"/data/gfsbin/manifest.txt" "/data/temp/manifest.txt"

# Acknowledgement of success
echo "===> maniFetched!!!\n"