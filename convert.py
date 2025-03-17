import sys
import struct
import binascii


def machex(mac):
    if isinstance(mac, list):  # Handle lists
        return [m.replace(":", "").upper() for m in mac]
    return mac.replace(':', '').upper()