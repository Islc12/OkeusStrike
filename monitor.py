#!/usr/bin/env python3

# WiFiSecAudit - monitor.py
# Copyright (C) 2025 Islc12
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import os
from datetime import datetime
import csv

device = None

def disable_monitor():
    global device
    if device is None:
        print("No device to disable, exiting...")
        exit()
    os.system(f"ip link set {device} down")
    os.system(f"iw dev {device} set type managed")
    os.system(f"ip link set {device} up")

    print("Monitor mode disabled")

'''Enables monitor mode and starts airdump-ng to view wireless networks. Also captures the output and sends it to a separate file.
    Assigns a file name to the capture file which is the current date and time from the time of capture. Also assigns the device 
    that we will be using throughout this script to a variable.'''
def monitor():
    global device
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    device = input("Enter the name of the network interface: ")
    file_name = f"CaptureFiles/capture_{timestamp}"
    os.system(f"ip link set {device} down")
    os.system(f"iw dev {device} set type monitor")
    os.system(f"ip link set {device} up")

    os.system(f"airodump-ng -w {file_name} --output-format csv {device}")

    csv_file = f"{file_name}-01.csv"
    return csv_file

def process_csv(csv_file):
    try:
        with open(csv_file, 'r') as file:
            print("Available networks:")
            print(f"{'BSSID':<22}{'Channel':<10}{'ESSID':<30}")
            print("-" * 60)
            lines = list(csv.reader(file))[2:-3]
            for line in lines:
                if line and len(line) > 0:
                    print(f"{line[0]:<20}{line[3]:<11}{line[-2]:<30}")
    except FileNotFoundError:
            print(f"{csv_file} not found.")
    except Exception as e:
        print(f"Error processing CSV: {e}")

def main():
    csv_file = None
    while True:
        try:
            print("Enter 1 to start monitoring and capture available networks\nEnter 2 to view available networks\nEnter 3 to proceed with packet sniffing\nEnter 99 to stop monitoring and exit\n")
            choice = int(input())
            print("")

            if choice == 1:
                csv_file = monitor()
            elif choice == 2:
                if csv_file:
                    process_csv(csv_file)
                elif not csv_file:
                    print("No capture file available. Please start monitoring first.\n")
            elif choice == 3:
                return True
            elif choice == 99:
                disable_monitor()
                exit()
            else:
                print("Invalid choice\n")
        except ValueError:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()