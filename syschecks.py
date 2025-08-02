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

import sys
import platform
import exit
import os

def sys_checks():
    if platform.system() != 'Linux':
        print("ATTENTION: This program is intended only to be run on GNU/Linux")
        sys.exit(exit.EXIT_NOT_LINUX)
    elif any(arg in sys.argv for arg in ("-h", "--help")):
        parser = argparse.ArgumentParser()
        parser.print_help()
        sys.exit(exit.EXIT_SUCCESS)
    elif os.geteuid() != 0:
        print("ATTENTION: Script requires root privlages, please run as root")
        sys.exit(exit.EXIT_NOT_ROOT)