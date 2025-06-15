import board
import digitalio
import time

# Green led is plugged into GP2
# Red led is plugged into GP15
# Button 1 is plugged into GP0
# Button 2 is plugged into GP16

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

greenled = digitalio.DigitalInOut(board.GP2)
greenled.direction = digitalio.Direction.OUTPUT

redled = digitalio.DigitalInOut(board.GP15)
redled.direction = digitalio.Direction.OUTPUT

button1 = digitalio.DigitalInOut(board.GP0)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP16)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

while True:
    if button1.value is False and button2.value is False:
        greenled.value = False
        redled.value = True

    elif button1.value is False or button2.value is False:
        greenled.value = True
        redled.value = False

    else:
        greenled.value = False
        redled.value = False
