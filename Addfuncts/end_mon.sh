#!/bin/bash

# script must be run as root!

ip link set wlan1 down
iw dev wlan1 set type managed
ip link set wlan1 up
iwconfig

