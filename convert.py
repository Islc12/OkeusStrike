import re

def machex(mac):
    mac_regex = r"^([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}$" # MAC address regex pattern

    def format_mac(m):
        if not re.match(mac_regex, m):
            print("Error: Invalid MAC address format")
            print("Correct format: AA:BB:CC:DD:EE:FF, AA-BB-CC-DD-EE-FF, or AAbbccddeeff")
            exit(1)
        return bytes.fromhex(m.replace(":", "").replace("-", ""))

    if isinstance(mac, list):  # Handle list of MACs
        return [format_mac(m) for m in mac]

    return format_mac(mac)