# See NOTES.md for documentation links
from board import NEOPIXEL, BTN
from digitalio import DigitalInOut, Direction, DriveMode, Pull
from neopixel_write import neopixel_write
import os
import random
import struct
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


# ============================================================================
# CONFIGURATION VALUES
# ============================================================================
# These two values determine the randomized delay between HID events. Base
# value is fixed. Noise value gets multiplied by a random value in range -0.5
# to 0.5 then added to the base to get the final value.
# Delay formula: seconds = base + ((random.random() - 0.5) * noise)
# CAUTION: Don't set this faster than human speed (might get yourself banned)
DELAY_BASE_S = 10.0
DELAY_NOISE_S = DELAY_BASE_S * 0.5

# These two values determine the keydown time (same method as for delay)
KEYDOWN_BASE_S = 0.180
KEYDOWN_NOISE_S = 0.090

# Maximum hours autoclicker will run before it automatically shuts itself off.
# Pets get hungry and stop aging if you AFK for too long between feedings.
MAX_AUTO_HOURS = 2/60   # TODO: change this from test value to real value

# Button press debounce interval
DEBOUNCE_S = 0.05
# ============================================================================
# SAFETY CHECKS: minimum 1 s delay between events, 50 ms keydown per event
assert DELAY_BASE_S - (DELAY_NOISE_S / 2) >= 1
assert KEYDOWN_BASE_S - (KEYDOWN_NOISE_S / 2) >= 0.05
# ============================================================================

# M5Stack AtomS3 Lite Neopixel color order is GRB
led = DigitalInOut(NEOPIXEL)
#led.switch_to_output(False, DriveMode.OPEN_DRAIN)
OFF = bytearray([0,0,0])
GREEN = bytearray([6,0,0])
AMBER = bytearray([7,7,0])

# Big button on top of AtomS3 Lite enclosure
btn = DigitalInOut(BTN)
led.switch_to_input(Pull.UP)


# This returns a value in the range of base_s ± plus_minus_s seconds
def randomize(base_s, noise_s):
    return base_s + ((random.random() - 0.5) * noise_s)

# Sleep for up to delay_seconds, ending early if button is pressed or the
# maximum auto mode timer expires.
def sleep_with_interrupt(button, delay_seconds, max_auto_s):
    end_s = min(time.monotonic() + delay_seconds, max_auto_s)
    while button.value and time.monotonic() < end_s:
        time.sleep(DEBOUNCE_S)
    time.sleep(DEBOUNCE_S)

def wait_for_idle(button):
    if not button.value:
        print("  Please let go of the button.")
        while not button.value:
            time.sleep(DEBOUNCE_S)
        print("  Thanks.")

def wait_for_release(button):
    # 1. Ensure button is not already pressed
    wait_for_idle(button)
    # 2. Wait for falling edge (button pressed)
    while button.value:
        time.sleep(DEBOUNCE_S)
    print("  press")
    # 3. Wait for rising edge (button released)
    while not button.value:
        time.sleep(DEBOUNCE_S)
    print("  release")

def send_HID_event(max_auto_s):
    print("Sending HID event...")
    neopixel_write(led, AMBER)
    seconds = randomize(KEYDOWN_BASE_S, KEYDOWN_NOISE_S)
    print("  keydown: %.3fs" % seconds)
    # SAFETY CHECK: Bail out if randomize gave an overly short interval
    assert seconds > 0.1, "randomized keydown delay was too short"
    if time.monotonic() + seconds > max_auto_s:
        return
    print("  TODO: type ' '")
    # TODO: HID key down
    sleep_with_interrupt(btn, seconds, max_auto_s)
    # TODO: HID key up
    neopixel_write(led, GREEN)

def main():
    # Poke the RGB LED to be sure it's turned off and ready for normal use
    time.sleep(0.5)
    neopixel_write(led, OFF)  # first write after boot will often glitch
    neopixel_write(led, OFF)  # but second write normally fixes it

    print("Starting autoclicker main event loop...")

    # Seed RNG with some hopefully good hardware generated entropy
    random.seed(struct.unpack("Q",os.urandom(8))[0])

    # Start the main loop
    while True:
        wait_for_idle(btn)
        print("Waiting for button press/release to start clicker...")
        wait_for_release(btn)
        print("=== CLICKER ACTIVATED! ===")
        # Inner loop ends when button pressed or max-auto timer expires
        max_auto_s = time.monotonic() + (MAX_AUTO_HOURS * 3600)
        while btn.value and time.monotonic() < max_auto_s:
            send_HID_event(max_auto_s)
            seconds = randomize(DELAY_BASE_S, DELAY_NOISE_S)
            # SAFETY CHECK: Bail out if randomize gave an overly short interval
            assert seconds >= 1, "main delay was too short"
            hours = (max_auto_s - time.monotonic()) / 3600
            print("Waiting...\n  next event: %d s\n  auto-off: %.3f hrs" %
                (seconds, hours))
            sleep_with_interrupt(btn, seconds, max_auto_s)
        # End of auto-click cycle. Update the various status indicators.
        if time.monotonic() >= max_auto_s:
            print("AUTO-OFF TIMER EXPIRED (%.3f hours)" % MAX_AUTO_HOURS)
        neopixel_write(led, OFF)
        print("=== CLICKER OFF ===")
        time.sleep(0.7)

main()
