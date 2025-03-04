#!/usr/bin/env python3

import os
import subprocess
from datetime import datetime

def disable_monitor():
    device = input("Enter the name of the network interface: ")
    os.system(f"ip link set {device} down")
    os.system(f"iw dev {device} set type managed")
    os.system(f"ip link set {device} up")

    print("Monitor mode disabled")

'''Enables monitor mode and starts airdump-ng to view wireless networks. Also captures the output and sends it to a separate file.
    Assigns a file name to the capture file which is the current date and time from the time of capture. Also assigns the device 
    that we will be using throughout this script to a variable.'''
def monitor():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    device = input("Enter the name of the network interface: ")
    file_name = f"capture_{timestamp}"
    os.system(f"ip link set {device} down")
    os.system(f"iw dev {device} set type monitor")
    os.system(f"ip link set {device} up")

    os.system(f"airodump-ng -w {file_name} --output-format csv {device}")

    # Used to format the output of the airdump-ng capture to a quick and easy to read format for the user to use later on
    awk_command = f'''awk 'NR<=2 {{next}} {{col1[NR]=$1; col6[NR]=$6; colSecondLast[NR]=$(NF-1)}} 
    END {{printf "%-19s %-9s %s\\n", "BSSID", "Channel", "ESSID"; for (i=3; i<NR-3; i++) 
    printf "%-10s %-1s %s\\n", col1[i], col6[i], colSecondLast[i];}}' {file_name}-01.csv | sed 's/,/     /g'
    '''
    # Used for debugging
    os.system(awk_command)

    
try:
    choice = int(input("Enter 1 to enable monitor mode, enter 2 to disable monitor mode: "))

    if choice == 1:
        monitor()
    elif choice == 2:
        disable_monitor()
    else:
        print("Invalid choice")
except ValueError:
    print("Invalid choice") 
