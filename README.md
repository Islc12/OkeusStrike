### Aircrack-ng suite automation script for passive network key interception

-------------------------------------------------------------------------------------------------------------------------------------------

### Disclaimer

This project includes the `rockyou.txt` wordlist for use with the `aircrack_ng` suite for educational and security testing purposes only.
Unauthorized use of this script or the wordlist to attack systems without permission is illegal and unethical. The creator of this
repository is not responsible for any misuse of the provided tools. Ensure you have explicit permission from the owner of any system you
are testing.

By using this repository, you agree to use it responsibly and comply with all relevant laws and regulations.

-------------------------------------------------------------------------------------------------------------------------------------------

Author: Rich Smith

Written: Feburary 2025

Contact: richrsmith@proton.me

-------------------------------------------------------------------------------------------------------------------------------------------

### Installation and setup instructions:
```
$ git clone https://github.com/Islc12/Air_H4ck.git
$ cd Air_H4ck
$ chmod u+x config.sh
$ ./config.sh
```

### Running the script:
```
# cd Air_H4ck
# ./air_hack.py
```

-------------------------------------------------------------------------------------------------------------------------------------------

### How to use:

Usage for this script is fairly simple, the most important though being is that it must be run as the root user due to how `airodump-ng`
functions. In the beginning of the script the user is prompted for two inputs, the first for the target AP's BSSID and the second for
channel to target for the BSSID. At this time this script does not feature channel hopping, in the future I will likely add that though.
If you don't know the target's BSSID or intended channel prior to running this script you can run `airodump-ng <wirelessinterface>` as root
and this will return a list of nearby AP's along with the BSSID and channel they're using. From there it's as simple as copy and paste 
into the appropriate input field. After this its just time to sit and wait. As this does a passive scan the script simply waits around for
a client to authenticate to the AP. Once that authentication happens and the 4-way handshake is caught the script will run begin to crack
the key using the `aircrack-ng` tool. By default this script uses the rockyou wordlist. However if `aircrack-ng` doesn't return a key with
the rockyou wordlist a capture file with the date and time (example: `capture_20250208_152133-01.cap`) is saved in the working directory.

------------------------------------------------------------------------------------------------------------------------------------------

### TODO:

1. Automate the monitor mode process
2. Log network discovery
3. Create a PKMID attack option
4. Add deauthentication script to force clients to re-authenticate
5. Add downgrade attack to force clients to downgrade wireless cryptographic protocols
6. Add evil twin attack to create a rogue AP
7. Add MITM attack to capture and decrypt traffic between client and AP
8. Give option to use MAC address spoofing
9. Give option to use a custom wordlist
10. Reveal hidden SSID's
