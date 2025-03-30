import network
import urequests
import time
from neopixel import Neopixel

# === Setup ===
ssid = 'Mohammad'
password = 'abbas000'

numpix = 144
strip = Neopixel(numpix, 0, 0, "RGB")
strip.brightness(50)

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
    leds_on = int(minutes_passed / 10)  # 1 LED = 10 minutes

    for i in range(numpix):
        if i < leds_on:
            strip.set_pixel(i, (0, 255, 0))  # Green
        else:
            strip.set_pixel(i, (0, 0, 0))    # Off
    strip.show()

# === Main Loop ===
connect_wifi()

while True:
    current_minutes = get_current_minutes()
    if current_minutes is not None:
        update_leds(current_minutes)
        print(f"🕒 {current_minutes} minutes into the day → {current_minutes / 1440:.1%} of the strip")
    else:
        print("⚠️ Skipping update due to API error")

    time.sleep(60)  # update every minute
