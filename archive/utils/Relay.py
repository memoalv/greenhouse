import RPi.GPIO as GPIO


class Relay:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def turnOn(self):
        try:
            GPIO.output(self.pin, True)
            return True
        except:
            return False

    def turnOff(self):
        try:
            GPIO.output(self.pin, False)
            return True
        except:
            return False
