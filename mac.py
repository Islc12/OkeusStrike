import socket
import sys
import struct
import binascii

def target(targmac):
    print(f"targmac() - {targmac}")

def source(sourcemac):
    print(f"sourcemac({sourcemac})")

def bssid(bssidmac):
    print(f"bssidmac({bssidmac})")

def macspoof(spoofmac):
    print(f"macspoof({spoofmac})")
