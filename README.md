# OkeusStrike - WiFi Deauthentication Attack Tool

#### Author: Rich Smith (Islc12)

#### Written: February 2025

#### Contact: richrsmith@proton.me

-------------------------------------------------------------------------------------------------------------------------------------------

## Disclaimer

This script is intended for educational and research purposes only. It is the responsibility of the user to ensure that their actions
comply with all applicable laws and regulations. The author and contributors of this script are not responsible for any misuse or illegal
activities conducted using this script. The use of this script for any illegal or unauthorized activities is strictly prohibited.

-------------------------------------------------------------------------------------------------------------------------------------------

## About

This tool is designed to help with penetration testing, ethical hacking, and network security assessments. It is currently in development
and is not yet ready for production use. However, despite being still in development, I have made it publicly available so that others can
see the progress and provide feedback.

-------------------------------------------------------------------------------------------------------------------------------------------

## Installation Instructions


### Basic Install/Configuration

- Get the repository from github
`$ git clone https://github.com/Islc12/OkeusStrike.git`
- Navigate to the cloned repository
`cd OkeusStrike`
- Add execute permissions
`chmod u+x okeus`


### Advanced Configuration

** perform basic instructions first **

- move `README.md` and `LICENSE` to the `/usr/share/doc/` directory
`# mv README.md LICENSE /usr/share/doc/`
- move the man page to the man1 directory
`# mv okeus.1.gz /usr/share/man/man1/`
- create a directory to move dependancies into
`# mkdir /usr/lib/OkeusStrike`
- move dependancies
`# mv *.py okeus /usr/lib/OkeusStrike`
- sym link to /usr/bin/
`# ln -s /usr/lib/OkeusStrike/okeus /usr/bin/okeus`

-------------------------------------------------------------------------------------------------------------------------------------------

## Usage Instructions:

All options (excluding `-h`, `--help`) require root priviledges to run.

Basic usage looks like such and will send a single deauthentication frame to the target destination at `11:22:33:44:55:66`, the program
will automatically fill in the source address using the provided network address. A valid interface is provided to tell the machine which
interface to use to send the deauth frame on.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1`

Similarly we can specify a source address, this can be either the same or different than the network address.
`# okeus -d 11:22:33:44:55:66 -s 99:88:77:66:55:44 -n aa:bb:cc:dd:ee:ff -i wlan1`

If we intend to broadcast deauth frames there is a built in `-b`, `--broadcast` option we can use in place of manually inputting the mac
address.
`# okeus -b -n aa:bb:cc:dd:ee:ff -i wlan1`

While advised, its not neccessary to use a reason code with the program. OkeusStrike will pad the reason code portion with 0's so that the
will send without producing a malformed packet error. At this time there are 66 unique reason codes to choose from. To add a reason code
we simple call the `--reason` arugment followed by the code we intend to use.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff --reason 3 -i wlan1`

Less likely to be used than any of the other options is the `--duration` option. This gives the user the ability to set the duration bytes.
There might be some exploits an experienced tester can find with this, which is why its included. Otherwise its not typically seen within 
an 802.11 frame and by default the bytes are set to \x00\x00. Duration bytes can be set from 1-65535.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --duration 10000`

We can also call on the `--fragment` or `--rand-frag` options to add fragmentation to the frame. For random fragmentation we simply need to
call the option, no additional value is required.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --rand-frag`
To manually add fragmentation we call the option and specify an integer from 1-15. Each frame send will have the same fragmentation number.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --fragment 10`

In addition to fragmentation, we can also set the sequence number within the sequence field. This can be done automatically using the
`--auto-seq` option, or manually using `--sequence`. Like with random fragmentation there is no need to specify any additional information
when using `--auto-seq`. The program will automatically increase the sequence bit.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --auto-seq`
To manually set the sequence number call `--sequence` followed by the sequence number. This can range from 1-4095. Each frame sent will
have the same sequence number.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --sequence 100`

Manual fragmentation and sequence input can be used together. Each frame will be sent using the same fragmentation and sequence number.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --fragment 5 --sequence 10`

Likewise random fragmentation and auto sequencing can also be used together to take care of some interesting way to craft a frame. By using
both `--rand-frag` and `--auto-seq` together the program will randomly cycle through fragmentation bits until, at random, a bit is chosen
that will end the random fragmentation and move the sequence bit 1 position up.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --rand-frag --auto-sequence`

`-f` or `--flood` gives us a unique method of sending deauth frames, that might not exactly perform as a deauth frame is traditionally
expected to. This option, by default, will send frames until the user interupts the program (ctrl + c) at a rate of 1 frame per .1 seconds.
This will send up to 600 deauth frames per minute to the intended target. No additional arguments are required with `--flood`.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --flood`

The `-c`, `--count` option gives the user to send a certain number of frames and once completed the program will end. This can be combined
with `--flood` to give the user increased flexibility. The below example will send 25 frames to `11:22:33:44:55:66` and then stop. Default
behavior is to send a single deauth frame.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 -c 25`

`--delay` allows the user to specify an amount of time between sending frames. This delay is specified in milliseconds. This option can be
used with `--flood` to give the user more flexibility. The below example shows a delay of 500 ms or .5 seconds between frames. Default
behavior is to send frames immediately with no delay (except with `--flood` as mentioned earlier).
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --delay 500`

By using the `--dry-run` option we are able to craft our custom deauth frames and run the program seeing output without actually sending
any packets. This is the intention for working in learning enviroments or to generate logs/documentation for testing.
`# okeus -d 11:22:33:44:55:66 -n aa:bb:cc:dd:ee:ff -i wlan1 --dry-run`

Minimal output will be shown without the `-v`, `--verbose` option. If you require extensive details for logging or reporting adding the
verbose option should produce sufficient information.

-------------------------------------------------------------------------------------------------------------------------------------------

## History

Okeus was a god of the Powhatan tribe located in Central/Eastern Virginia, USA. He's associated as the God of war and often considered
vengeful or wrathful. Mistakenly considered the devil by early European colonists as well as missionaries, Okeus was likely to be the most
important God in the Powhatan pantheon. He was often worshiped by the Powhatan as they believed that he would bring good fortunes during
times of illness, crop failures, and other disasters.

Reference Link: [Okeus History](https://en.wikipedia.org/wiki/Okeus)

-------------------------------------------------------------------------------------------------------------------------------------------

## License
This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.
