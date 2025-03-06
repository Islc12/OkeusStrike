### Aircrack-ng suite automation script for passive network key interception

-------------------------------------------------------------------------------------------------------------------------------------------

### Disclaimer

This script is intended for educational and research purposes only. It is the responsibility of the user to ensure that their actions
comply with all applicable laws and regulations. The author and contributors of this script are not responsible for any misuse or illegal
activities conducted using this script. The use of this script for any illegal or unauthorized activities is strictly prohibited.

-------------------------------------------------------------------------------------------------------------------------------------------

### Author: Rich Smith (Islc12)

### Written: Feburary 2025

### Contact: richrsmith@proton.me

-------------------------------------------------------------------------------------------------------------------------------------------

### License
This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

-------------------------------------------------------------------------------------------------------------------------------------------

### Installation Instructions

`pip install -r requirements.txt`

-------------------------------------------------------------------------------------------------------------------------------------------

## Wordlist Usage
This script requires a wordlist for brute-force attacks. Due to licensing concerns, `rockyou.txt` is **not included** in this repository.  
However, you can obtain it from a Kali Linux installation or other legal sources:  

- **Kali Linux Path:** `/usr/share/wordlists/rockyou.txt.gz` (extract using `gunzip rockyou.txt.gz`)  
- **Online:** Various security research repositories provide commonly used wordlists.  
- **Custom Wordlist:** You can specify any wordlist file when running the script. 

-------------------------------------------------------------------------------------------------------------------------------------------

### Installation and setup instructions:
```
$ git clone https://github.com/Islc12/WiFiSecAudit.git
$ cd WifiSecAudit
$ chmod u+x config.sh
$ ./config.sh
```

### Running the script:
```
# cd WifiSecAudit
# ./main.py
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
11. Create a log file that documents each step taken during the audit for future reference when writing your report

MUCH LATER ON - potential useful features
1. Add a location tracking feature to document GPS coordinates of where the audit was performed
    - This could be a useful feature if performing an audit on a large scale such as a warehouse or campus
2. Create a floor plan layout feature to map out the location of the audit
    - This could be a useful feature when performing to show exact location of the audit
    - Shows AP overlay locations on the floor plan
    - Shows AP signal strength on the floor plan
