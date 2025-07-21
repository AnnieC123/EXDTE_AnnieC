import board
import digitalio
import analogio
import pwmio
import time
import random
from adafruit_debouncer import Debouncer

# Variables:
MIN_TIME = 1.0
MAX_TIME = 5.0
DEFAULT = 100
high_score = DEFAULT

# Setting up the button
button_pin = digitalio.DigitalInOut(board.GP1)
button_pin.direction = digitalio.Direction.INPUT
button_pin.pull = digitalio.Pull.UP
my_button = Debouncer(button_pin)


# Setting up the leds
blueled = digitalio.DigitalInOut(board.GP0)
blueled.direction = digitalio.Direction.OUTPUT
greenled = digitalio.DigitalInOut(board.GP2)
greenled.direction = digitalio.Direction.OUTPUT


# Generate random time function
def randtime_generator():
    random_time = random.uniform(MIN_TIME, MAX_TIME)
    return(random_time)

# runs when you beat the highscore
def beat_highscore():
        high_score = user_score
        print("You beat your highscore!")
        greenled.value = True
        time.sleep(0.5)
        greenled.value = False
        time.sleep(0.5)
        greenled.value = True
        time.sleep(0.5)
        greenled.value = False

# Main code
while True:
    my_button.update()
    if my_button.rose is True:
        blueled.value = False
        print("Starting...")
        # Breaks out of this code after user starts the game
        break
    # Blue LED is on, indicating the game is on standby
    if my_button.value is True:
        blueled.value = True
    time.sleep(0.1)


# Calls random time generator to generate a random time
button_time = (randtime_generator())
# Sleeps for random time
time.sleep(button_time)
# light turns on / records current time
lighton_time = time.monotonic()
while True:
    my_button.update()
    blueled.value = True
    if my_button.fell is True:
        # Calculates user reaction time
        user_score = time.monotonic() - lighton_time
        print(f"your reaction time is {user_score}")
        if user_score < int(high_score):
            beat_highscore()
        else:
            print("You didn't beat your highscore.")


"""while True:
    my_button.update()


    if my_button.rose is True:
        print("Just released")
        blueled.value = False

    if my_button.fell is True:
        print("Just pressed")
        blueled.value = True

    if my_button.value is True:
        print("not pressed")
        blueled.value = False

    if my_button.value is False:
        print("pressed")
        blueled.value = True

    time.sleep(0.5)"""


