# this is the final code that you need this will light up the amunt of led lights using the leds.
# by using the time api. 

import network
import urequests
import time
import sys
import select
from neopixel import Neopixel

# === Setup ===
ssid = 'Sheraj'
password = 'rigbykc12345'

numpix = 60
strip = Neopixel(numpix, 0, 0, "RGB")
strip.brightness(50)

last_update_time = time.time()  # Track last automatic update
event_time_minutes = None  # Store event time in minutes (None if no event set)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    print("Connecting to WiFi...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("\n✅ Connected! IP:", wlan.ifconfig()[0])

def get_current_minutes():
    try:
        response = urequests.get("https://timeapi.io/api/TimeZone/zone?timezone=America/New_York")
        data = response.json()
        response.close()

        time_str = data["currentLocalTime"]  # Format: '2025-03-29T13:45:20'
        hour, minute = map(int, time_str.split("T")[1].split(":")[:2])
        return hour * 60 + minute
    except Exception as e:
        print("Failed to fetch time:", e)
        return None

def update_leds(minutes_passed):
    """Update LEDs based on the progress of the day"""
    if minutes_passed is None:
        print("⚠️ Skipping LED update due to invalid time")
        return

    leds_on = int(minutes_passed / 24)  # 1 LED = 24 minutes

    # Update the progress bar (green LEDs)
    for i in range(numpix):
        if i < leds_on:
            strip.set_pixel(i, (0, 255, 0))  # Green for progress
        else:
            strip.set_pixel(i, (0, 0, 0))    # Off

    # If an event time is set, keep the corresponding LED red
    if event_time_minutes is not None:
        # Calculate the LED position for the event time
        event_led_position = int((event_time_minutes / 1440) * numpix)
        strip.set_pixel(event_led_position, (255, 0, 0))  # Red for event

    strip.show()

def blink_leds():
    """Blink the currently lit LEDs three times instantly"""
    print("✨ Blinking LEDs...")

    # Save current LED state
    current_minutes = get_current_minutes()
    if current_minutes is None:
        return  # Don't blink if time data isn't available

    for _ in range(3):
        # Turn off LEDs
        for i in range(numpix):
            strip.set_pixel(i, (0, 0, 0))
        strip.show()
        time.sleep(0.2)  # Shorter delay for faster blinking

        # Restore LEDs to progress state
        update_leds(current_minutes)
        time.sleep(0.2)

    print("✅ Blinking complete, resuming automatic mode")

def set_led_for_time(time_str):
    """Set the LED corresponding to the entered time"""
    global event_time_minutes  # Use global variable to store event time

    try:
        # Parse time from HH:MM
        hour, minute = map(int, time_str.split(":"))
        event_time_minutes = hour * 60 + minute
        print(f"Event set for time {time_str}, LED at position {int((event_time_minutes / 1440) * numpix)}")

        # Immediately update LEDs to reflect the event time
        current_minutes = get_current_minutes()
        if current_minutes is not None:
            update_leds(current_minutes)

    except Exception as e:
        print(f"⚠️ Error: {e}. Please enter time in HH:MM format.")

print("🖥️ Ready to receive serial commands and update LEDs based on time!")
connect_wifi()
update_leds(get_current_minutes())  # Initialize the LED strip

while True:
    # === Check for Serial Commands ===
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        command = sys.stdin.readline().strip().lower()
        if command == "blink":
            blink_leds()
        elif ":" in command:  # If the command is a time in HH:MM format
            set_led_for_time(command)
        else:
            print(f"⚠️ Unknown command: {command}")

    # === Automatic Time-Based LED Update (Runs Every 60s) ===
    if time.time() - last_update_time >= 60:
        current_minutes = get_current_minutes()
        if current_minutes is not None:
            update_leds(current_minutes)
            print(f"🕒 {current_minutes} minutes into the day → {current_minutes / 1440:.1%} of the strip")
        else:
            print("⚠️ Skipping update due to API error")
        last_update_time = time.time()
    
    time.sleep(0.1)  # Short sleep to keep checking for serial commands frequently






