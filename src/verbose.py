# OkeusStrike - Advanced Deauthentication Attack Tool - verbose.py
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

from . import (
    assemble,
    fragseq,
    radio,
    okeusargs,
    reason
    )
from datetime import datetime

args = okeusargs.parse_arguments()
td = datetime.now().strftime("Today's Date: %Y-%m-%d\nCurrent Time: %H:%M:%S")

def verb(interface=None, source_mac=None, reason_code=None, randfrag=False, autoseq=False, body_bytes=None):
    sq = fragseq.fs(frag=args.fragment, seq_num=args.sequence, randfrag=args.randomfrag, autoseq=args.autoseq)
    f_ctl, f_frag, f_dur, ct, src, net, ch, src_n_v = assemble.f_assem(dest_mac=args.dest, broadcast_attack=args.broadcast, source_mac=args.ap_source, network_bssid=args.net_bssid, frag=args.fragment, dur=args.duration, randfrag=args.randomfrag)
    radiotap_header, it_version, it_pad, it_len, it_present = radio.ieee80211_radiotap_header()

    print("-" * 100)
    print(td)
    if not source_mac:
        print(src_n_v)
    print(f"Interface: {interface}")
    print("-" * 100)
    print(f"{'Frame composition'.center(100)}")
    print("-" * 100)
    print(f"Radiotap version: {it_version.hex()}")
    print(f"Radiotap pad: {it_pad.hex()}")
    print(f"Radiotap length: {it_len.hex()}")
    print(f"Radiotap fields present: {it_present.hex()}")
    print(f"Frame type: {f_ctl.hex().upper()} (Deauthentication)")
    print(f"Fragmentation set: {f_frag.hex()} - type: {ch}")
    print(f"Duration: {f_dur.hex().upper()}")
    print(f"Destination: {ct.hex().upper()}")
    print(f"Source: {src.hex().upper()}")
    print(f"Network: {net.hex().upper()}")
    if not (autoseq or randfrag):
        print(f"Sequence Control: {sq.hex().upper()}")
    if (autoseq or randfrag):
        print("Sequence Control: DYNAMIC")
    match args.reason_code:
        case None:
            print(f"Reason Code: {reason.reasoncode_input(0).hex()} - {reason.def_code(0)}")
        case _:
            print(f"Reason Code: {reason.reasoncode_input(args.reason_code).hex()} - {reason.def_code(args.reason_code)}")
    print(f"Body padding: {args.body_pad} null bytes padded")
    print("-" * 100)