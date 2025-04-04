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
    1: ('<H', x01), # - Code 1: Unspecified reason. - \x00\x01
    2: ('<H', x02), # - Code 2: Previous authentication is no longer valid. - \x00\x02
    3: ('<H', x03), # - Code 3: Station has left the Basic Service Set (BSS) or Extended Service Set (ESS). - \x00\x03
    4: ('<H', x04), # - Code 4: Inactivity timer expired. - \x00\x04
    5: ('<H', x05), # - Code 5: Disassociated due to insufficient resources at the AP. - \x00\x05
    6: ('<H', x06), # - Code 6: Class 2 frame received from a nonauthenticated station. - \x00\x06
    7: ('<H', x07), # - Code 7: Class 3 frame received from a nonassociated station. - \x00\x07
    8: ('<H', x08), # - Code 8: Station has left the BSS or ESS (disassociation). - \x00\x08
    9: ('<H', x09), # - Code 9: Station is attempted to authenticate with an AP that doesn't support the authentication protocol. - \x00\x09
    10: ('<H', x0A), # - Code 10: Specified timeout - \x00\x0A
    11: ('<H', x0B), # - Code 11: Group Key Update Timeout - \x00\x0B
    12: ('<H', x0C), # - Code 12: Unspecified reason (disassociation). - \x00\x0C
    13: ('<H', x0D), # - Code 13: Invalid information - \x00\x0D
    14: ('<H', x0E) # - Code 14: Incompatible parameters - \x00\x0E
    }

    rc = reasoncode.get(reason)
    return rc