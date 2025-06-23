import board
import digitalio
import time
from adafruit_debouncer import Debouncer

# Setting up the button
button_pin = digitalio.DigitalInOut(board.GP12)
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP
my_button = Debouncer(button_pin)

# Setting up the LEDs
greenled = digitalio.DigitalInOut(board.GP17)
greenled.direction = digitalio.Direction.OUTPUT
redled = digitalio.DigitalInOut(board.GP16)
redled.direction = digitalio.Direction.OUTPUT

while True:
    my_button.update()
    if my_button.value is True:
        print("not pressed")
        greenled.value = False
        redled.value = False
    if my_button.value is False:
        print("pressed")
        greenled.value = True
        redled.value = True
    if my_button.fell is True:
        print("Just pressed")
        greenled.value = True
        redled.value = False
    if my_button.rose is True:
        print("Just released")
        greenled.value = False
        redled.value = True
    time.sleep(0.5)

