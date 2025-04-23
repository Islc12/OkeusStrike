## This is a list of running to do's for the development of OkeusStrike. To do's aren't in any particular order of importance.

- Correct issue with improper mode of network interface:

Currently the program will send frames even when the interface type is not in monitor mode. This of course results in no frames being sent.
The program however believes that it is sending frames and does not raise any errors.
	
	
- Add channel switching functionality:

At the moment users must set a channel manually, either using `iw`, `iwconfig`, or whatever other utility they chose to use. While not
critical for usage, its kind of annoying to have to set it elsewhere and to increase the "scriptibility" of this program I'd much rather
something like this be able to be set from the program itself rather than to have to call another tool or program to do it.
	
	
- Correct choices in the arguments file to not display a range of choices upon incorrect input:

Right now if a user were to input an out of range value of certain arguments (reason, fragment, duration, etc.) the help menu would appear.
While the help menu appearing is something that we want, what we don't want to see is every single choice for that arguement written out. 
While its not a big deal for an argument like fragment that only has values of 1-15, it becomes a problem with the arguments that have many 
more choices available. Users don't need to see 65,535 choices ranging from 1 to 65,535 because they mistakenly typed the wrong value for
the duration argument after all.
	
	
- Test functionality within virtual machines:

As of now I have not tested to see how OkeusStrike performs while running in a virtual machine, this may produce some unintended results.
	
	
- Test functionality across various distrubtions:

OkeusStrike was developed on my Fedora 41 (and later 42) machine, I have not tested it on other RH based distrobutions nor any Debian based
distrobutions or any other types of Linux distros. While I have no intention on making sure its compatible with every Linux distro, I would
like to see it function correctly across the major distro's.
	
	
- Correct random fragmentation with auto sequencing:

Right now the random fragment argument will simply roll a random integer and use that to fill in the fragmentation bit. This can result in
repeating rolls, which is fine if thats all the user chooses when doing manual sequencing. However, when the user engages auto sequencing we
shouldn't have to see the same roll for a fragmentation bit occur more than once within the same sequence number. If frames are dropped OTA
that is one thing, but the target shouldn't recieve a fragmentation of 5 on a sequence of 3 more than once. This needs to be randomized better
so that the fragmentation number increases only, and then after a certain random value (between lets say 8-15) it will auto sequence to the
next sequence bit.
	
	
- Add body byte argument:

For the purposes of confusing a target we're going to give the user the ability to add bytes to the body of the 802.11 frame. I'm not sure if
we want to let the user create a custom byte package or simply pad the body with `\x00` and the user specify how many bytes they want to use.

### More will be added in time

-------------------------------------------------------------------------------------------------------------------------------------------

## License
This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.