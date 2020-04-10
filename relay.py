import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RELAYS = {"f":26, "b":19, "l":13, "r":6}

GPIO.setup(list(RELAYS.values()), GPIO.OUT, initial=GPIO.LOW)
cleanup=GPIO.cleanup

BUTTONS_OFF = {"f":False, "b":False, "l":False, "r":False}

def update_relays(buttons=BUTTONS_OFF):
    for k, pin in RELAYS.items():
        GPIO.output(RELAYS[k], not buttons[k])
    
