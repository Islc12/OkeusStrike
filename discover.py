# OkeusStrike - Advanced Deauthentication Attack Tool - discover.py
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

import socket
import string
import time

def disc(interface):
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003)) # creates a raw socket for capturing packets
        s.bind((interface, 0)) # binds the socket to the specified interface and port

        disc_net = set() # set to store unique network names - set is used to avoid duplicates

        print("\nScanning for networks, press CTRL+C to stop\n")
        print(f"{'BSSID':<20}{'SSID'.center(20)}{'Channel'.center(10)}{'Frequency Band'.center(16)}{'Signal Strength'.center(20)}{'MFP Required'.center(12)}{'MFP Enabled'.rjust(14)}")
        print("-" * 112)
        while True:
            try:
                p = s.recvfrom(2048)[0] # recieves packet from socket, up to 2048 bytes, extracts raw packet data

                # needed to locate the size of the radiotap header to offset the  frame control field
                rt_len = int.from_bytes(p[2:4], "little")  # Extract radiotap header length, bytes 2 and 3, little endian format
                chanfreq = int.from_bytes(p[18:20], "little") # Extract channel frequency, bytes 18 and 19, little endian format
                sig = p[22] # Extract signal strength, byte 22
                sigstr = int(sig) - 256 # Convert signal strength to dBm

                # Parse the MAC header and RSN capabilities to determine MFP support
                mac_head = rt_len  # Radiotap header length
                fcf = p[mac_head:mac_head + 2]  # Frame Control Field (2 bytes)
                fcf_flags = int.from_bytes(fcf, "little")  # Convert FCF to an integer
                mac_head_len = 24  # Base MAC header length

                # Check the To DS and From DS flags (bits 8 and 9 of FCF)
                to_ds = (fcf_flags & 0x0100) >> 8
                from_ds = (fcf_flags & 0x0200) >> 9
                if to_ds and from_ds:
                    mac_head_len += 6  # Add Address 4 field (6 bytes)

                # Check QoS Control (bit 12 of FCF)
                qos_control = (fcf_flags & 0x1000) >> 12
                if qos_control:
                    mac_head_len += 2  # Add QoS Control field (2 bytes)

                # Check HT Control (bit 13 of FCF)
                ht_control = (fcf_flags & 0x2000) >> 13
                if ht_control:
                    mac_head_len += 4  # Add HT Control field (4 bytes)

                rsn_start = mac_head + mac_head_len # Move to RSN Capabilities

                # Find RSN Information Element (tag 0x30) starting from RSN start
                rsn_tag = 0x30
                rsn_index = p.find(bytes([rsn_tag]), rsn_start)

                # Extract RSN Information Element length
                length = p[rsn_index + 1]  # Length of RSN IE
                rsn_data = p[rsn_index + 2:rsn_index + 2 + length]

                # Extract RSN Capabilities (last 2 bytes of RSN data)
                rsn_capabilities = int.from_bytes(rsn_data[-2:], "little")

                # Determine MFP support
                mfp_capable = (rsn_capabilities & 0x0080) >> 7  # Bit 7
                mfp_required = (rsn_capabilities & 0x0100) >> 8  # Bit 8

                # Map results to human-readable values
                mfp_enabled = "Y" if mfp_capable else "N"
                mfp_required = "Y" if mfp_required else "N"
                
                # calculate channel number based on frequency
                if 2412 <= chanfreq <= 2472:
                    channel = (chanfreq - 2407) // 5
                    freq_band = "2.4 GHz"
                elif 5170 <= chanfreq <= 5825: # This won't work for all wifi adapters, as most only seem to pickup 2.4 GHz in monitor mode
                    channel = (chanfreq - 5000) // 5
                    freq_band = "5 GHz"
                else:
                    channel = None
            
                frame_ctrl = p[rt_len:rt_len + 2] # collects the first two bytes of the frame control field
                frame_type = (frame_ctrl[0] >> 2) & 0x03 # checks bits 2 and 3 of the first byte to determine frame type (ie management, control, data)
                frame_subtype = (frame_ctrl[0] >> 4) & 0x0F # checks bits 4 thru 7 to determine frame subtype (ie beacon, probe request, etc.)
                
                if frame_type == 0 and frame_subtype == 8: # check if beacon frame - \x08
                    bssid = ":".join(format(x, "02x") for x in p[rt_len + 16:rt_len + 22]) # extract BSSID
                    ssid_len = p[rt_len + 37] # determine SSID length 
                    ssid_raw = p[rt_len + 38:rt_len + 38 + ssid_len] # offset to ssid from Radiotap header
                    ssid = "".join(chr(x) if chr(x) in string.printable else "" for x in ssid_raw) # convert ssid bytes to string
                    
                    if (bssid, ssid) not in disc_net: # check if network has already been discovered
                        print(f"{bssid:<20}{ssid.center(20)}{str(channel).center(10)}{freq_band.center(16)}{(str(sigstr) + ' dBm').center(20)}{mfp_required.center(12)}{mfp_enabled.rjust(14)}") # print network info
                        disc_net.add((bssid, ssid)) # if not discovered, add to set
    
            # used to handle network interuptions - typically caused by additional network services such as NetworkManager
            except OSError as e:
                if e.errno == 100: # errno 100 is a common error code for "Network is Down"
                    time.sleep(1) # sleep for half a second to give the network a chance to recover
                    continue # handles gracefully and allows the program to continue scanning
                else:
                    raise e # re-raises the exception if it is not a network down error
            except IndexError: # handles index errors that may occur when accessing the packet data due to corrupted to malformed packets
                continue

    except KeyboardInterrupt: # allows the program to gracefully handle keyboard interrupts
        print("\nScan completed.")

    except Exception as e: # handles any other exceptions that may occur
        print(f"An error occurred: {e}")
    
    finally: # gives a final cleanup step
        s.close() # closes out the socket


def client_disc(bssid, interface):
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
        s.bind((interface, 0))

        client_disc = set()

        print("\nScanning for networks, press CTRL+C to stop\n")
        while True:
            try:
                p = s.recvfrom(2048)[0]

                # Enter code here

            except OSError as e:
                if e.errno == 100:
                    time.sleep(1)
                    continue
                else:
                    raise e
            except IndexError:
                continue

    except KeyboardInterrupt:
        print("\nScan completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        s.close()

if __name__  == "__main__":
    disc()
    client_disc()