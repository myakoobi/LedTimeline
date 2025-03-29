import network
import urequests
import time

ssid = 'Mohammad'
password = 'abbas000'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to WiFi...")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(1)
print("\n✅ Connected! IP:", wlan.ifconfig()[0])

# Example 1: Query Google
print("\n1. Querying google.com:")
r = urequests.get("http://www.google.com")
print("Google response length:", len(r.content))
r.close()

# Example 2: Query UTC time from a working API
print("\n2. Querying the current GMT+0 time:")
r = urequests.get("http://worldtimeapi.org/api/timezone/Etc/UTC")
data = r.json()
print("UTC Time:", data["datetime"])
r.close()
