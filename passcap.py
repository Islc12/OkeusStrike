#!/usr/bin/env python3

# WiFiSecAudit - A WiFi Security Auditing Script - passcap.py
# Copyright (C) 2025 Richard Smith (Islc12)
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
import subprocess
import time
from datetime import datetime

# Run as root
if os.geteuid() != 0:
    print("ATTENTION: Script requires root privlages, please run as root")
    exit(1) 

def inputs():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    file_name = f"CaptureFiles/pass_cap_{timestamp}"
    bssid = input("Enter target AP BSSID: ")
    channel = int(input("Enter target AP channel: "))
    wordlist = input("Enter the path to your wordlist file: ")

    return file_name, bssid, channel, wordlist

def airodump(file_name, bssid, channel, device):
    # Starts airodump-ng and waits for the capture file to appear.
    cap_file = f"{file_name}-01.cap"
    airodump_cmd = ["airodump-ng", "-d", bssid, "-c", str(channel), "-w", file_name, "--output-format", "pcap", device]
    airodump_proc = subprocess.Popen(airodump_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    time.sleep(2) # Give time to initalize the capture file

    if os.path.exists(cap_file):
        print(f"Capture file found: {cap_file}")
    else:
        print(f"Capture file not found: {cap_file}")
        print(f"Error: {airodump_proc.stderr.read().decode()}")
        airodump_proc.terminate()
        return None, airodump_proc  # Ensure it still returns a tuple

    return cap_file, airodump_proc

def tshark(device):
    # Monitors the capture file for EAPOL packets.
    file_name, bssid, channel, wordlist = inputs()
    cap_file, airodump_proc = airodump(file_name, bssid, channel, device)

    time.sleep(2)  # Give time to start filling the file
    print("Checking for EAPOL packets...")

    eapol_count = set()
    try:
        while eapol_count != 4:
            cmd = ["tshark", "-r", cap_file, "-Y", "eapol", "-l"]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

            for line in process.stdout:
                print(line.strip())
                if "Message 1 of 4" in line:
                    eapol_count.add(1)
                elif "Message 2 of 4" in line:
                    eapol_count.add(2)
                elif "Message 3 of 4" in line:
                    eapol_count.add(3)
                elif "Message 4 of 4" in line:
                    eapol_count.add(4)

                if len(eapol_count) == 4:
                    print("4-way handshake captured.")
                    return
                else:
                    print(sorted(list(eapol_count)))
                    time.sleep(1)

            process.wait()
            time.sleep(1) 

    finally:
        airodump_proc.terminate()
        return cap_file, wordlist

def crack(cap_file, wordlist):
    aircrack_cmd = ["aircrack-ng", "-w", wordlist, cap_file]
    aircrack_proc = subprocess.run(aircrack_cmd, text=True, capture_output=True)
    print(aircrack_proc.stdout)

def main(device):
    cap_file, wordlist = tshark(device)
    crack(cap_file, wordlist)
