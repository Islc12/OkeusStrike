# OkeusStrike - Advanced Deauthentication Attack Tool - mac.py
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
import sys
import struct
import binascii

def target(targmac):
    print(f"targmac() - {targmac}")

def source(sourcemac):
    print(f"sourcemac({sourcemac})")

def bssid(bssidmac):
    print(f"bssidmac({bssidmac})")
