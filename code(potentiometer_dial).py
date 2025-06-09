import time
import board
import analogio
import pwmio

knob = analogio.AnalogIn(board.A0)
led = pwmio.PWMOut(board.GP2, frequency=1000)

while True:
    print("raw = " + str(knob.value))
    led.duty_cycle = knob.value
    time.sleep(0.5)
