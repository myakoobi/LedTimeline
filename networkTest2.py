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
try:
    r = urequests.get("http://www.google.com")
    print("Google response length:", len(r.content))  # Print response length
    r.close()
except Exception as e:
    print("Failed to fetch Google:", e)

# Example 2: Query the current time using timeapi.io
print("\n2. Querying the current time from timeapi.io:")
try:
    r = urequests.get("https://timeapi.io/api/TimeZone/zone?timezone=Europe/Bucharest")  
    data = r.json()
    print("Current Time in Bucharest:", data["currentLocalTime"])  
    r.close()
except Exception as e:
    print("Failed to fetch time:", e)

