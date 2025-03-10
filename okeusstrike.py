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

import socket # low level networking
import argparse # argument parsing
import os # interact with underlying OS
from datetime import datetime # apply for file naming
import subprocess # possibly use to run native linux commands
import time # use for time based attack types
import glob # use for file navigation of captured files
import csv # reading/writing csv log files
import logging # build log files
import pyshark # packet capture system
