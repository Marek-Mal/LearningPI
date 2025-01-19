import gpiozero
import time
import RPi.GPIO as gpio

led = gpiozero.LED(17)

i = 0

while True:
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)
    i += 1
    if i == 20 :
        break

gpio.cleanup()
