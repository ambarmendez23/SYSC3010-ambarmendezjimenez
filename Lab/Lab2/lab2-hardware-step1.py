import sense_hat
from time import sleep

sense = sense_hat.SenseHat()
current_letter = 0

def show_m():
    global current_letter
    sense.show_letter("M")
    current_letter = 1

def show_s():
    global current_letter
    sense.show_letter("A")
    current_letter = 2
    
pressed = sense_hat.ACTION_PRESSED
sense.clear()

while True:
    
        for event in sense.stick.get_events():
                if event.action == pressed:
                    if current_letter == 0:
                        show_m()
                    elif current_letter == 1:
                        show_s()
                    else:
                        show_m()
