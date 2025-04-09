# OkeusStrike - Advanced Deauthentication Attack Tool - okeusarguments.py
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

import argparse

class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        """
        Adjusts the help text alignment.
        """
        super().__init__(prog, max_help_position=100)  # Ensures descriptions align correctly

    def _format_action_invocation(self, action):
        """
        Keeps metavar close to the option flag.
        """
        if action.option_strings:
            option_str = ", ".join(action.option_strings)
            metavar = self._format_args(action, action.dest.upper()) if action.metavar else ""
            return f"  {option_str} {metavar}"
        else:
            return super()._format_action_invocation(action)

def parse_arguments():
    parser = argparse.ArgumentParser(description="OkeusStrike: Advanced Deauthentication Attack Tool", formatter_class=CustomHelpFormatter)

    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="Enable verbose output")

    parser.add_argument("-i", "--interface", dest="netinterface", required=True, metavar="<INTERFACE>", type=str, help="Network interface ID")

    parser.add_argument("-d", "--dest", dest="dest", metavar="<DESTINATION>", type=str, help="Target destination MAC address(es)")
    parser.add_argument("-s", "--source", dest="ap_source", type=str, metavar="<SOURCE_MAC>", help="Source MAC address")
    parser.add_argument("-n", "--network", dest="net_bssid", type=str, metavar="<BSSID>", help="BSSID of the target network")
    parser.add_argument("-b", "--broadcast", action="store_true", dest="broadcast", help="Broadcast attack")

    parser.add_argument("--delay", dest="delay", type=int, metavar="<TIME_IN_MS>", help="Time delay between frames in milliseconds")

    parser.add_argument("-f", "--flood", dest="flood", action="store_true", help="Flood attack, cannot be used with --count, floods until interupt")

    parser.add_argument("-c", "--count", dest="count", type=int, metavar="<INT>", help="Number of frames to send, cannot be used with --flood")

    parser.add_argument("--fragment", dest="fragment", type=int, metavar="<[1-15]>", choices=range(1,16), help="Set fragmentation bits")
    parser.add_argument("--sequence", dest="sequence", type=int, metavar="<[1-4095]>", choices=range(1,4096), help="Sequence number for deauthentication frame, default is None")

    parser.add_argument("--random-frag", dest="randomfrag", action="store_true", help="Randomize fragmentation")
    parser.add_argument("--auto-seq", dest="autoseq", action="store_true", help="Automatically increment sequence control")

    parser.add_argument("-r", "--reason", choices=range(1,67), metavar="<[1-66]>", dest="reason_code", type=int, help="Reason code for deauthentication")

    parser.add_argument("--duration", dest="duration", metavar="<[1-65535]>", choices=range(1,65536), type=int, help="Set duration bytes")

    parser.add_argument("--dry-run", dest="dryrun", action="store_true", help="Runs OkeusStrike without sending packets")

    return parser.parse_args()

if __name__ == "__main__":
    arguments()