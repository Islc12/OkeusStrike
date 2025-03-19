import socket
import time

def deauthflood(seconds):
    print(f"Deauth Flood seconds: {seconds}")

def broadcast():
    print("\xFF\xFF\xFF\xFF\xFF\xFF")

if __name__ == "__main__":
    broadcast()
    deauthflood()

