from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)


def a():
    W = white
    O = nothing
    logo = [
    O, O, O, W, W, O, O, O, 
    O, O, W, O, O, W, W, O,
    O, W, O, O, O, O, W, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, W, O, O, O, O, W, O,
    O, W, O, O, O, O, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo
def m():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, W, O, O, W, O, O, O,
    O, W, W, W, W, O, O, O,
    O, O, W, W, O, O, O, O,
    ]
    return logo


images = [a,m] 
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
    
