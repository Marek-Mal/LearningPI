# Using PIR sensor detect movment in the room
import gpiozero
import time
import RPi.GPIO as gpio

pir = gpiozero.MotionSensor(4)

while True:
    time.sleep(0.01)
    print(pir.motion_detected)