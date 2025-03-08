#!/usr/bin/env python3

# WiFiSecAudit - A WiFi Security Auditing Script - sortfiles.py
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
import glob
import csv

def sortfile():
    # Directory containing the capture files
    sd = "CaptureFiles"
    directory = os.path.join(os.getcwd(), sd)

    # Get a list of all .cap files matching the pattern
    files = glob.glob(os.path.join(directory, "capture_*.csv"))

    # Sort files by name (lexicographically correct due to the timestamp format)
    files.sort()

    # Get the newest file (last one in sorted order)
    newest_file = files[-1] if files else None

    return newest_file

def process_csv(newest_file):
    try:
        with open(newest_file, 'r') as file:
            print("Available networks:")
            print(f"{'BSSID':<22}{'Channel':<10}{'ESSID':<30}")
            print("-" * 60)
            lines = list(csv.reader(file))[2:-3]
            for line in lines:
                if line and len(line) > 0:
                    print(f"{line[0]:<20}{line[3]:<11}{line[-2]:<30}")
    except FileNotFoundError:
            print(f"{newest_file} not found.")
    except Exception as e:
        print(f"Error processing CSV: {e}")

def main():
    newest_file = sortfile()
    if newest_file:
        print(f"Viewing file: {newest_file}\n")
        process_csv(newest_file)
    else:
        print("No capture files found.")

if __name__ == "__main__":
    main()