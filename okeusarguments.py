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

    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    parser.add_argument("-w", "--write", type=str, metavar="<USER_INPUT>_YYmmdd_HHMMSS.pcap", dest="writefile", help="Write capture data to pcap file")

    parser.add_argument("-i", "--interface", dest="netinterface", required=True, metavar="<INTERFACE>", type=str, help="Network interface to use")
 
    parser.add_argument("-d", "--discover", dest="discover_networks", action="store_true", help="Discover available networks")
    parser.add_argument("--client-discover", dest="client_discover", metavar="<NETWORK_BSSID>", type=str, help="Scan for clients on Network BSSID")    

    parser.add_argument("-c", "--channel", dest="channel", metavar="<CHANNEL_NUMBER>", type=int, help="Channel to use")
    parser.add_argument("-p", "--power", dest="power", metavar="<POWER_LEVEL>", type=int, help="Set the transmit power in dBm")

    parser.add_argument("-t", "--target", dest="target", metavar="<TARGET>", nargs="+", type=str, help="Target client MAC address(es)")
    parser.add_argument("-s", "--source", dest="ap_source", type=str, metavar="<SOURCE_MAC>", help="Source MAC address")
    parser.add_argument("-n", "--network", dest="net_bssid", type=str, metavar="<BSSID>", help="BSSID of the target network")
    parser.add_argument("-b", "--broadcast", action="store_true", dest="broadcast", help="Broadcast attack")

    parser.add_argument("--time", dest="time", type=int, metavar="<TIME_IN_MS>", help="Time delay between frames in milliseconds")

    parser.add_argument("--flood", dest="flood", type=int, metavar="<TIME_IN_SECONDS>", help="Flood attack with time duration in seconds, cannot be used with --count, default is a 5 second frame flood")

    parser.add_argument("--count", dest="count", type=int, metavar="<INT>", help="Number of frames to send, cannot be used with --flood")

    parser.add_argument("--fragment-size", dest="fragment_size", metavar="<INT>", type=int, help="Fragment size")
    parser.add_argument("--sequence", dest="sequence", type=int, metavar="<SEQUENCE_NUMBER>", help="Sequence number for deauthentication frame, default is None")

    parser.add_argument("--reason-code", choices=range(1,15), metavar="<REASON_CODE>", dest="reason_code", type=int, help="Reason code for deauthentication")

    parser.add_argument("--duration", dest="duration", metavar="<TIME_IN_MS>", type=int, help="Duration of the attack in milliseconds")

    return parser.parse_args()

if __name__ == "__main__":
    arguments()