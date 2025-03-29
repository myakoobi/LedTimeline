import network
import time
import wifi  # the wifi.py file you created

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(wifi.ssid, wifi.password)

        timeout = 10  # seconds
        while not wlan.isconnected() and timeout > 0:
            print(".", end="")
            time.sleep(1)
            timeout -= 1

    if wlan.isconnected():
        print("\nConnected to WiFi!")
        print("IP Address:", wlan.ifconfig()[0])
    else:
        print("\nFailed to connect.")

connect()
