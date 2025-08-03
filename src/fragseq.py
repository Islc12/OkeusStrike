# OkeusStrike - Advanced Deauthentication Attack Tool - fragseq.py
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
import random

def fs(frag=None, seq_num=None, randfrag=False, autoseq=False):
    # upgrade this to a match case statement to clean it up
    
    if not hasattr(fs, "sn"):
        fs.sn = 1
    if all(x is None for x in (frag, seq_num)) and not (randfrag or autoseq):
        seq = struct.pack('<H', 0x00)

    if randfrag and not (frag or seq_num or autoseq):
        rf = random.randint(1, 14)
        seq = struct.pack('<H', rf & 0x0F)
    elif autoseq and not (frag or seq_num or randfrag):
        seq = struct.pack('<H', (fs.sn << 4) & 0xFFF0)
        fs.sn += 1
    elif (autoseq and randfrag) and not (seq_num or frag):
        rf = random.randint(1, 14)
        if rf >= 8:
            seq = struct.pack('<H', ((fs.sn << 4) & 0xFFF0) | (rf & 0x0F))
            fs.sn += 1
        else:
            seq = struct.pack('<H', (fs.sn << 4) & 0xFFF0)
    elif (randfrag and seq_num) and not (frag or autoseq):
        rf = random.randint(1, 14)
        seq = struct.pack('<H', ((seq_num << 4) & 0xFFF0) | (rf & 0x0F))
    elif frag and not (seq_num or randfrag or autoseq):
        seq = struct.pack('<H', frag & 0x0F)
    elif (frag and autoseq) and not (randfrag or seq_num):
        seq = struct.pack('<H', ((fs.sn << 4) & 0xFFF0) | (frag & 0x0F))
        fs.sn += 1
    elif (frag and seq_num) and not (randfrag or autoseq):
        seq = struct.pack('<H', ((seq_num << 4) & 0xFFF0) | (frag & 0x0F))
    elif (seq_num) and not (frag or randfrag or autoseq):
        seq = struct.pack('<H', ((seq_num << 4) & 0xFFF0) )

    return seq