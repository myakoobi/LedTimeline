import machine
import time
import neopixel

# GPIO pin where DIN is connected
led_pin = machine.Pin(0)

# Number of LEDs on your strip
num_leds = 144

# Set up the NeoPixel object
strip = neopixel.NeoPixel(led_pin, num_leds)

# Function to fill the strip with a color
def set_color(r, g, b):
    for i in range(num_leds):
        strip[i] = (r, g, b)
    strip.write()

# Example: Set all LEDs to red
set_color(255, 0, 0)

# Keep it on
while True:
    time.sleep(1)