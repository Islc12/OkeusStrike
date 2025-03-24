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

def machex(mac):
    mac_regex = r"^([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}$" # MAC address regex pattern

    def format_mac(m):
        if not re.match(mac_regex, m):
            print("Error: Invalid MAC address format")
            print("Correct format: AA:BB:CC:DD:EE:FF, AA-BB-CC-DD-EE-FF, or AAbbccddeeff")
            exit(1)
        return bytes.fromhex(m.replace(":", "").replace("-", ""))

    if isinstance(mac, list):  # Handle list of MACs
        return [format_mac(m) for m in mac]

    return format_mac(mac)