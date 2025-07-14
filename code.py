import board
import digitalio
import time

# Setting up the LEDs
greenled = digitalio.DigitalInOut(board.GP17)
greenled.direction = digitalio.Direction.OUTPUT
redled = digitalio.DigitalInOut(board.GP16)
redled.direction = digitalio.Direction.OUTPUT

start_time = time.monotonic()

while start_time + 3 > time.monotonic():
    greenled.value = True
    time.sleep(0.1)
    greenled.value = False
    time.sleep(0.1)
redled.value = True
