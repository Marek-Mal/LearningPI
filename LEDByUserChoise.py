import gpiozero
import time
import RPi.GPIO as gpio

led = gpiozero.LED(17)

while True:
    user_input = int(input('Type 1 to turn on LED or 0 To turn it off: '))
    if user_input == 1:
        led.on()
    elif user_input == 0:
        led.off()
    else:
        break

gpio.cleanup