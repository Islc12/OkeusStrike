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
import arguments  # Parsing command-line arguments from arguments.py
import os  # Interact with the underlying OS
import time  # Time-based attack types (delays, duration, etc.)
import glob  # File navigation for captured files
import csv  # Reading/writing CSV log files
import pyshark  # Packet capture system
import struct  # Unpacking binary data (e.g., network headers)
import binascii  # Convert between binary and ASCII representations
import fcntl  # Low-level network interface control (e.g., setting flags)
import select  # Non-blocking I/O and socket timeout handling
import errno  # Handling OS-level network errors
import sys  # System-specific functionality (e.g., exiting on errors)
import itertools  # Iterating over values (useful for fragmentation/sequencing)
import random  # Randomization (delays, MAC spoofing, sequence numbers)
from datetime import datetime  # File naming based on timestamps
import threading # multithreading for file writing while capturing/attacking


# Check if the script is running with root privileges, exits if not
if os.geteuid() != 0:
    print("ATTENTION: Script requires root privlages, please run as root")
    exit(1) 

def main():
    args = arguments.parse_arguments()
    # Parse command-line arguments
    write_file = args.writefile
    interface = args.netinterface
    discover = args.discover_networks
    client_discovery = args.client_discover
    net_channel = args.channel
    power_level = args.power
    target_macs = args.target
    source_mac = args.ap_source
    network_bssid = args.net_bssid
    multiple = args.multiple_file
    broadcast_attack =  args.broadcast
    time_delay = args.time
    rand_interaval = args.random_interval
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
    socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    socket.bind((interface, 0))

    # handle all illogical arguments
    if write_file and not (discover or client_discovery or target_macs):
        exit(1)
    if frame_flood and (num_frames or time_delay or rand_interval or dur_of_attack or rand_dur or discover or client_discovery):
        exit(1)
    if num_frames and client_discovery:
        exit(1)
    if time_delay and rand_interval:
        exit(1)
    if target_macs and (multiple or client_discovery):
        exit(1)
    if rand_frag and frag_size:
        exit(1)
    if sequence_number and rand_sequence:
        exit(1)
    if dur_of_attack and rand_dur:
        exit(1)
    if discover and (client_discovery or target_macs or num_frames):
        exit(1)
    
    # start logic
    if discover:
        disc()
        if write_file:
            create_file()
    if client_discovery:
        xmac = machex(client_discovery)
        bssid(xmac)
        if write_file:
            create_file()
        if net_channel:
            channelinput(net_channel)
