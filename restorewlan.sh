#!/bin/bash

# This script checks if you are connected to your router.
# To make it run periodically in the background you need to do
# the following:
#
# Create cronjob as root by entering 'sudo crontab -e' and copying
# the following line to the end of the file (without the '#'):
#
# */5 * * * * sh /home/pi/Downloads/EnviroPi/restorewlan.sh
#
# NOTES: 1) You might need to adjust the path to 'restorewlan.sh'
#	 2) You might need to adjust the IP below to the one of your router
#	 3) You might need to make the script executable (chmod +x restorewlan.sh)

# If routers IP cannot be pinged restart wlan0
if ! [ "$(ping -c 1 192.168.0.1)" ]; then
    echo "WLAN DOWN - RESTARTING INTERFACE"
    sudo ifdown --force wlan0
    sudo ifup wlan0
fi
echo "WLAN SEEMS OK"
