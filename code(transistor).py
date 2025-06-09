import time
import board
import analogio
import digitalio

# Setup analog imput (knob)
knob = analogio.AnalogIn(board.A0)

# Setup the GPIO pin to control the transistor (as digital output)
transistor_pin = digitalio.DigitalInOut(board.GP15)
transistor_pin.direction = digitalio.Direction.OUTPUT

while True:
    # Read analog value (0 to 65535)
    analog_value = knob.value

    print("raw = " + str(knob.value))

    # Calculate delay based on analog input divded by 20,000
    delay_time = analog_value / 20000

    # Turns the LEDs on by setting transistor pin HIGH
    transistor_pin.value = True
    print(f"LEDs ON for {delay_time:.2f} seconds")
    time.sleep(delay_time)

    # Turn LEDs OFF
    transistor_pin.value = False
    print(f"LEDs OFF for {delay_time:.2f} seconds")
    time.sleep(delay_time)
