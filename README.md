# USB HID Autoclicker

**[DRAFT: WORK IN PROGRESS]**

This is a USB HID hardware autoclicker to prevent AFK kicks in Grow a Garden on
Roblox. The code tells the AtomS3 Lite to present itself as an HID keyboard.
The keyboard types spaces on a timer to make your avatar jump. Jumping resets
the AFK timer so you don't get kicked. Normally, people do this with software,
but using CircuitPython is safer (some free autoclickers have malware).

The point of staying logged in is to help with farming fruit mutations, which
happen slower when you're offline. Roblox will kick you after 20 minutes
of inactivity. Computers often have a screen saver or sleep mode that activates
at 5 or 10 minutes of idle. So, the code here makes your avatar jump at random
intervals in the range of 1 to 5 minutes.

CAUTION: Using a misconfigured autoclicker has the potential to get you banned
from a game or banned from Roblox. Before you use this, familiarize yourself
with the Roblox terms of service and check if there are any additional rules
for games you play. From what I read, Roblox and game developers mainly care
about preventing cheating and protecting their servers from excessive network
traffic. For example, if you set an autoclicker for a 5ms interval and leave it
running, that would send tons of network packets. Also, certain games might
consider clicking faster than a human to be a form of cheating.

As far as I can tell, nobody particularly cares if you use an autoclicker to
prevent AFK kicks in Grow a Garden, **as long as** the input events happen at
human speed. If anything, the devs seem to like high concurrent user numbers.
But, that might change in the future, so use your own judgement and keep an eye
out for rules changes.


## Hardware

- [M5Stack AtomS3 Lite](https://www.digikey.com/en/products/detail/m5stack-technology-co-ltd/C124/18070571)
- USB C cable
- Spare computer with Roblox installed


## Usage

After flashing the firmware .bin file from circuitpython.org and installing the
autoclicker project bundle code.py:

1. Ensure the AtomS3 Lite is plugged into the computer with Roblox.

2. In Roblox, log into your private Grow a Garden server (to avoid getting
   your fruits stolen while AFK), then feed your pets or whatever else you need
   to do to get ready.

3. Find a good spot for your avatar to stand.

4. Press the big button on the AtomS3 Lite. The LED should turn dim red with a
   bump in brightness each time the autoclicker types a space.

5. The autoclicker will shut itself off automatically after 9 hours. To turn it
   off earlier, press the big button on the AtomS3 Lite. The LED should turn
   off.
