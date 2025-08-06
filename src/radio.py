# OkeusStrike - Advanced Deauthentication Attack Tool - radio.py
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

# This needs to get expanded upon, more information is available at the radiotap source code at https://github.com/radiotap/radiotap-library
# They also have a .py version available, depending on the nature of it I may fork that and bring it over here, though that largely depends
# upon the dependancies that are involved in it as the primary way I am designing Okeus is to be reliant on very little (if any) 3rd parties.
def ieee80211_radiotap_header():
    it_version = struct.pack('B', 0x00)
    it_pad = struct.pack('B', 0x00)
    it_len = struct.pack('<H', 0x08)
    it_present = struct.pack('4B', 0x00, 0x00, 0x00, 0x00)
    radiotap_header = it_version + it_pad + it_len + it_present
    return radiotap_header, it_version, it_pad, it_len, it_present