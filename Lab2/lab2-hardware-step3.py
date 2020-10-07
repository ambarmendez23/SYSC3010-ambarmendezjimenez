from sense_hat import SenseHat
from time import sleep

s=SenseHat()
red= (255,0,0)
green=(0,255,0)
blue=(0,0,255)

def temperature():
    temp = s.get_temperature()
    print(temp)
    
    if temp > 50:
        s.clear(red)
    
    elif temp < 50 and temp > 24:
        s.clear(green)
    
    elif temp < 24 and temp > 0:
        s.clear(blue)

    sleep(1)
    s.show_message(str(round(temp,2)))


while True:
    for event in s.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                temperature()
            sleep(0.5)
    
