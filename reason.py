# OkeusStrike - Advanced Deauthentication Attack Tool - input.py
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

def reasoncode_input(reason):
    reasoncode = {
    1: struct.pack('<H', 0x01), # - Code 1: Unspecified reason. - \x00\x01
    2: struct.pack('<H', 0x02), # - Code 2: Previous authentication is no longer valid. - \x00\x02
    3: struct.pack('<H', 0x03), # - Code 3: Station has left the Basic Service Set (BSS) or Extended Service Set (ESS). - \x00\x03
    4: struct.pack('<H', 0x04), # - Code 4: Inactivity timer expired. - \x00\x04
    5: struct.pack('<H', 0x05), # - Code 5: Disassociated due to insufficient resources at the AP. - \x00\x05
    6: struct.pack('<H', 0x06), # - Code 6: Class 2 frame received from a nonauthenticated station. - \x00\x06
    7: struct.pack('<H', 0x07), # - Code 7: Class 3 frame received from a nonassociated station. - \x00\x07
    8: struct.pack('<H', 0x08), # - Code 8: Station has left the BSS or ESS (disassociation). - \x00\x08
    9: struct.pack('<H', 0x09), # - Code 9: Station is attempted to authenticate with an AP that doesn't support the authentication protocol. - \x00\x09
    10: struct.pack('<H', 0x0A), # - Code 10: Specified timeout - \x00\x0A
    11: struct.pack('<H', 0x0B), # - Code 11: Group Key Update Timeout - \x00\x0B
    12: struct.pack('<H', 0x0C), # - Code 12: Unspecified reason (disassociation). - \x00\x0C
    13: struct.pack('<H', 0x0D), # - Code 13: Invalid information - \x00\x0D
    14: struct.pack('<H', 0x0E) # - Code 14: Incompatible parameters - \x00\x0E
    }

    rc = reasoncode.get(reason)
    return rc

def def_code(reason):
    code_def = {
    1: "Code 1: Unspecified reason.",
    2: "Code 2: Previous authentication is no longer valid",
    3: "Code 3: Station has left the Basic Service Set (BSS) or Extended Service Set (ESS)",
    4: "Code 4: Inactivity timer expired",
    5: "Code 5: Disassociated due to insufficient resources at the AP",
    6: "Code 6: Class 2 frame received from a nonauthenticated station",
    7: "Code 7: Class 3 frame received from a nonassociated station",
    8: "Code 8: Station has left the BSS or ESS (disassociation)",
    9: "Code 9: Station is attempted to authenticate with an AP that doesn't support the authentication protocol",
    10: "Code 10: Specified timeout",
    11: "Code 11: Group Key Update Timeout",
    12: "Code 12: Unspecified reason (disassociation)",
    13: "Code 13: Invalid information",
    14: "Code 14: Incompatible parameters"
    }

    cd = code_def.get(reason)
    return cd