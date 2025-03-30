# the lights cannot be light up without this file or library neo pixel



from neopixel import Neopixel
import utime

numpix = 60
strip = Neopixel(numpix, 0, 0, "RGB")

color = (0, 100, 100)  # Blue color

delay = 0.05
strip.brightness(42)

while True:
    # Light up each pixel one by one
    for i in range(numpix):
        strip.set_pixel(i, color)
        strip.show()
        utime.sleep(delay)
    
    # Turn off each pixel one by one
    for i in range(numpix):
        strip.set_pixel(i, (0, 0, 0))
        strip.show()
        utime.sleep(delay)

