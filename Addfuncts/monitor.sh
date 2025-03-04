#!/bin/bash

# script must be run as root!

 ip link set wlan1 down
 iw dev wlan1 set type monitor
 ip link set wlan1 up

 airodump-ng wlan1
