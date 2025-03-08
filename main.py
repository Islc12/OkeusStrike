#!/usr/bin/env python3

# WiFiSecAudit - A WiFi Security Auditing Script - main.py
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
from datetime import datetime
import subprocess
from sortfiles import main as display_networks
from passcap import main as pass_scan
#from deauth import main as deauth_main
#from downgrade import main as downgrade_main

def main():
    print("Welcome to WiFiSecAudit")
    device = input("Enter the name of the NIC you wish to use: ")
    while True:
        print("""
        Select an option:
        1. Start monitor mode
        2. Begin network identification
        3. View avaiable target networks
        4. Passive network scan (with packet capture)
        5. Deauthentication attack
        6. Downgrade attack
        7. ** Reserved ** - Evil twin?
        8. ** Reserved ** - Mac spoofing?
        9. ** Reserved ** - MIMT?
        10. ** Reserved ** - PKMID?
        99. End monitor mode and exit""")

        try:
            choice = int(input("Enter your choice: "))
            #device = input("Enter the name of the network interface: ")
            print("")
            if choice == 1:
                os.system(f"ip link set {device} down")
                os.system(f"iw dev {device} set type monitor")
                os.system(f"ip link set {device} up")
                continue
            elif choice == 2:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M")
                file_name = f"CaptureFiles/capture_{timestamp}"
                airodump_cmd = ["airodump-ng", "-w", file_name, "--output-format", "csv", device]
                subprocess.run(airodump_cmd)
                #os.system(f"airodump-ng -w {file_name} --output-format csv {device}")
                continue
            elif choice == 3:
                display_networks()
            elif choice == 4:
                net_scan = pass_scan(device)
                continue
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                pass
            elif choice == 8:
                pass
            elif choice == 9:
                pass
            elif choice == 10:
                pass
            elif choice == 99:
                os.system(f"ip link set {device} down")
                os.system(f"iw dev {device} set type managed")
                os.system(f"ip link set {device} up")

                print("Monitor mode disabled")
                exit(1)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
    return device

if __name__ == "__main__":
    main()