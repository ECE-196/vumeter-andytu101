import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

filtered_volume = 0

rise_factor = 1.0  
fall_factor = 0.95  

# main loop
while True:
    volume = microphone.value

    print(volume)

    if volume > filtered_volume:
        filtered_volume = volume
    else:
        filtered_volume = filtered_volume * fall_factor

    for x in range(0, 11):
        if filtered_volume > 22000 + (x * 2600):
            leds[x].value = 1
        else:
            leds[x].value = 0

    sleep(0.05)  
    

    
    
    #added code to test
    #leds[2].value = not leds[0].value

    

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?