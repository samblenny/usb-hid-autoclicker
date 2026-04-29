# USB HID Autoclicker

This is a USB HID hardware autoclicker to prevent AFK kicks in Grow a Garden on
Roblox. The code tells the AtomS3 Lite to present itself as an HID keyboard.
The keyboard types spaces on a timer to make your avatar jump. Jumping resets
the AFK timer so you don't get kicked. Normally, people do this with software,
but using CircuitPython is safer (some free autoclickers have malware).

The point of staying logged in is to help with farming fruit mutations, which
happen slower when you're offline. Roblox will kick you after 20 minutes
of inactivity. Computers often have a screen saver or sleep mode that activates
at 5 or 10 minutes of idle. The code here will type the spacebar at randomized
intervals about once or twice a minute.

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

3. Find a good spot for your avatar to stand. For lower CPU use and less fan
   noise, you might try going to the opposite corner of the map away from your
   garden and looking off over the edge toward empty sky. You can also turn off
   VFX and audio options in the settings menu.

4. Press the big button on the AtomS3 Lite. The LED should turn amber while
   it's pressing the spacebar and green while it's waiting to press the next
   one.

5. The autoclicker will shut itself off automatically after 9 hours. To turn it
   off earlier, press the big button on the AtomS3 Lite. The LED should turn
   off when the clicker has stopped.

CAUTION: For this to work, you need to  leave your operating system's window
manager focused on the Roblox window. Otherw ise, you'll end up with random
spaces typed into whate ver other window you switched the focus to. If you try
to work on the Roblox  computer while this is running, you'll get ran dom
spaces inserted into whatever  app you have open. I recommend using a spare
computer for ru nning the AFK autoclicker.
