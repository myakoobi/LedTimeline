from neopixel import Neopixel
import utime

numpix = 144  # or however many LEDs you actually connected
strip = Neopixel(numpix, 0, 0, "RGB")  # GPIO0 is your data pin

strip.brightness(50)  # adjust to your liking

# Initial hue offset
hue_offset = 0

while True:
    for i in range(numpix):
        # Spread hue across the strip and offset over time
        hue = (hue_offset + (i * 65536 // numpix)) % 65536
        r, g, b = strip.colorHSV(hue, 255, 255)
        strip.set_pixel(i, (r, g, b))
    strip.show()
    hue_offset = (hue_offset + 256) % 65536  # shift hue over time
    utime.sleep(0.05)  # control speed of the rainbow
