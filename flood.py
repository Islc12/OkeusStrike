# OkeusStrike - Advanced Deauthentication Attack Tool - massatk.py
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

import socket
import time
from okeus import f_assem

def deauthflood(seconds):
    if seconds == -1:
        while True:
            #spam flooding
    elif seconds > 0:
        # flood for {seconds}
    else:
        print("Invalid time")
        exit(1)
    print(f"Deauth Flood seconds: {seconds}")

