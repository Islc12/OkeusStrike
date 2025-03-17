#!/usr/bin/env python3

# WiFiSecAudit - okeusstrike
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

# not all these imports are used in the final code, they are here until I determine exactly which file they will be used in
import socket  # Low-level networking with raw sockets
import okeusarguments # Parsing command-line arguments from arguments.py
import discover # Network discovery functions from discovery.py
import convert # MAC address conversion from convert.py
import powerchan # Power level adjustment from powerchange.py
import output # File output functions from output.py
import mac # Handles target, source and bssid flags
import input

import os  # Interact with the underlying OS
import time  # Time-based attack types (delays, duration, etc.)
import glob  # File navigation for captured files
import struct  # Unpacking binary data (e.g., network headers)
import binascii  # Convert between binary and ASCII representations
import fcntl  # Low-level network interface control (e.g., setting flags)
import select  # Non-blocking I/O and socket timeout handling
import errno  # Handling OS-level network errors
import sys  # System-specific functionality (e.g., exiting on errors)
import itertools  # Iterating over values (useful for fragmentation/sequencing)
import threading # multithreading for file writing while capturing/attacking

# Check if the script is running with root privileges, exits if not
if os.geteuid() != 0:
    print("ATTENTION: Script requires root privlages, please run as root")
    exit(1) 

def main():
    args = okeusarguments.parse_arguments()
    # Parse command-line arguments
    write_file = args.writefile # mapped
    interface = args.netinterface # handled automatically
    net_discovery = args.discover_networks # mapped
    client_discovery = args.client_discover # mapped
    net_channel = args.channel # mapped
    power_level = args.power # mapped
    target_macs = args.target # mapped
    source_mac = args.ap_source # mapped
    network_bssid = args.net_bssid # mapped
    multiple = args.multiple_file # sort of mapped - still need to read the file, parse it into machex and then into target_macs
    broadcast_attack =  args.broadcast
    time_delay = args.time
    rand_interval = args.random_interval
    frame_flood = args.flood
    num_frames = args.count
    rand_frag = args.random_fragment
    frag_size = args.fragment_size
    sequence_number = args.sequence
    rand_sequence = args.randomize_sequence
    mac_spoof = args.spoof
    reason = args.reason_code
    dur_of_attack = args.duration
    rand_dur = args.randomize_duration

    # Create a raw socket for capturing packets
    #socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    #socket.bind((interface, 0))

    # handle all illogical arguments
    #if write_file and not (net_discovery or client_discovery or target_macs):
    #    exit(1)
    #if frame_flood and (num_frames or time_delay or rand_interval or dur_of_attack or rand_dur or net_discovery or client_discovery):
    #    exit(1)
    #if num_frames and client_discovery:
    #    exit(1)
    #if time_delay and rand_interval:
    #    exit(1)
    #if target_macs and (multiple or client_discovery):
    #    exit(1)
    #if rand_frag and frag_size:
    #    exit(1)
    #if sequence_number and rand_sequence:
    #    exit(1)
    #if dur_of_attack and rand_dur:
    #    exit(1)
    #if net_discovery and (client_discovery or target_macs or num_frames):
    #    exit(1)
    
    # start logic
    if net_discovery:
        discover.disc()
    if write_file:
        output.create_file(write_file)
    if client_discovery:
        xmac = convert.machex(client_discovery)
        discover.client_disc(xmac)
    if net_channel:
        powerchan.channelinput(net_channel)
    if power_level:
        powerchan.powerinput(power_level)
    if target_macs:
        xmac = convert.machex(target_macs)
        mac.target(xmac)
    if source_mac:
        xmac = convert.machex(source_mac)
        mac.source(xmac)
    if network_bssid:
        xmac = convert.machex(network_bssid)
        mac.bssid(xmac)
    if multiple:
        # in development
        input.multiple_input(multiple)

if __name__ == "__main__":
    main()