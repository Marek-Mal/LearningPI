# This program powers on the led light while the button is being pressed
import gpiozero
import RPi.GPIO as gpio
import signal

button = gpiozero.Button(26)
led = gpiozero.LED(17)

button.when_pressed = led.on
button.when_released = led.off

signal.pause()

# UNOPTIMIZED !
# while True:
#     if button.is_pressed:
#         led.on()
#     else:
#         led.off()

