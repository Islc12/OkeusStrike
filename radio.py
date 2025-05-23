# OkeusStrike - Advanced Deauthentication Attack Tool - rt.py
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

def rt_head():
    v = struct.pack('B', 0x00)
    pad = struct.pack('B', 0x00)
    length = struct.pack('<H', 0x08)
    prsnt = struct.pack('4B', 0x00, 0x00, 0x00, 0x00)
    rth = v + pad + length + prsnt
    return rth, v, pad, length, prsnt