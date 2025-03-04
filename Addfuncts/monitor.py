#!/usr/bin/env python3

import os
import subprocess

def disable_monitor():
    device = input("Enter the name of the network interface: ")
    os.system(f"ip link set {device} down")
    os.system(f"iw dev {device} set type managed")
    os.system(f"ip link set {device} up")

    print("Monitor mode disabled")

def monitor():
    device = input("Enter the name of the network interface: ")
    os.system(f"ip link set {device} down")
    os.system(f"iw dev {device} set type monitor")
    os.system(f"ip link set {device} up")

    os.system(f"airodump-ng {device}")
    
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
