#!/usr/bin/env python3

# OkeusStrike - Advanced Deauthentication Attack Tool - convert.py
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

import re
import struct

def machex(mac):
    mac_regex = r"^([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}$|^[0-9a-fA-F]{12}$"  # Allow colon, dash, or plain format

    def format_mac(m):
        if not re.match(mac_regex, m):
            print("Error: Invalid MAC address format")
            print("Correct format: AA:BB:CC:DD:EE:FF, AA-BB-CC-DD-EE-FF, or AABBCCDDEEFF")
            exit(1)
        
        clean_mac = m.replace(":", "").replace("-", "").lower()
        mac_bytes = [int(clean_mac[i:i+2], 16) for i in range(0, 12, 2)]
        return struct.pack('!6B', *mac_bytes)

    return format_mac(mac)
