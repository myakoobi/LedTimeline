import network
import time

ssid = "YourHotspotName"
password = "YourHotspotPassword"

def connect():
    print("Trying to connect to Wi-Fi...")
    print("SSID:", ssid)
    print("Password:", password)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        wlan.connect(ssid, password)

        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            print(".", end="")
            time.sleep(1)
            timeout -= 1

    if wlan.isconnected():
        print("\n✅ Connected!")
        print("IP Address:", wlan.ifconfig()[0])
    else:
        print("\n❌ Failed to connect.")

connect()
