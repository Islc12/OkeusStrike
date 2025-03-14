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