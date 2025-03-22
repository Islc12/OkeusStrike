import socket
import string
import time

def disc(interface):
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003)) # creates a raw socket for capturing packets
        s.bind((interface, 0)) # binds the socket to the specified interface and port

        disc_net = set() # set to store unique network names - set is used to avoid duplicates

        print("\nScanning for networks, press CTRL+C to stop\n")
        print(f"{'BSSID':<20}{'SSID'.center(20)}{'Channel'.center(10)}{'Frequency Band'.center(16)}{'Signal Strength'.center(20)}{'MFP Enabled'.rjust(12)}")
        print("-" * 100)
        while True:
            try:
                p = s.recvfrom(2048)[0] # recieves packet from socket, up to 2048 bytes, extracts raw packet data

                # needed to locate the size of the radiotap header to offset the  frame control field
                rt_len = int.from_bytes(p[2:4], "little")  # Extract radiotap header length, bytes 2 and 3, little endian format
                chanfreq = int.from_bytes(p[18:20], "little") # Extract channel frequency, bytes 18 and 19, little endian format
                sigstr = p[22] # Extract signal strength, byte 22
                
                # calculate channel number based on frequency
                if 2412 <= chanfreq <= 2472:
                    channel = (chanfreq - 2407) // 5
                    freq_band = "2.4 GHz"
                elif 5170 <= chanfreq <= 5825:
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
                        print(f"{bssid:<20}{ssid.center(20)}{str(channel).center(10)}{freq_band.center(16)}{(str(sigstr) + ' dBm').center(20)}{mfp_enabled.rjust(12)}") 
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

    #except Exception as e: # handles any other exceptions that may occur
        #print(f"An error occurred: {e}")    
    
    finally: # gives a final cleanup step
        s.close() # closes out the socket


def client_disc(bssid):
    print(f"client_disc({bssid})")

if __name__  == "__main__":
    disc()
    client_disc()