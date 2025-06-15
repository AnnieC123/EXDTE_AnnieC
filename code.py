import board
import pwmio
import analogio

knob = analogio.AnalogIn(board.A0)
greenled = pwmio.PWMOut(board.GP17, frequency=1000)
redled = pwmio.PWMOut(board.GP16, frequency=1000)
while True:
    knob_value = knob.value
    if knob_value < 65535/2:
        greenled.duty_cycle = knob_value*2
        redled. duty_cycle = 0
    else:
        greenled.duty_cycle = 65535
        redled.duty_cycle = (knob_value - 32768)*2
    print(knob_value)
