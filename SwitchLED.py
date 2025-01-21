# This code requires any number led lights installed on a breadboard to work. It switches witch led is light up based on button press
import gpiozero
import time
import RPi.GPIO as gpio
import signal

ledRED = gpiozero.LED(17)
ledGREEN = gpiozero.LED(27)
ledYELLOW = gpiozero.LED(22)
led_list = [ledRED, ledGREEN, ledYELLOW]
lenght_list = len(led_list)
ledRED.on()
button = gpiozero.Button(26, bounce_time=0.05) # BOUNCE TIME 

def changeLED():
    for i in range(lenght_list):
        if led_list[i].is_active:
            led_list[i].off()
            if i+1 == lenght_list:
                led_list[0].on()
            else:
                led_list[i+1].on()
            break
        
        # elif led_list[i].is_active == False and led_list[i-1].is_active == False:
        #     led_list[0].on()

    # if ledYELLOW.is_active:
    #     ledYELLOW.off()
    #     ledRED.on()
    # elif ledRED.is_active:
    #     ledRED.off()
    #     ledGREEN.on()
    # elif ledGREEN.is_active:
    #     ledGREEN.off()
    #     ledYELLOW.on()
    # else:
    #     ledRED.on()
    

button.when_pressed = changeLED

signal.pause()

gpio.cleanup()