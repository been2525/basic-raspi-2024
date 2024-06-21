import RPi.GPIO as GPIO
import time

pirPin = 24
red = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(red, GPIO.OUT)

try:
	while True:
		if GPIO.input(pirPin) == True:
			print("Detected")
			GPIO.output(red, False)
			time.sleep(1)
		else:
			GPIO.output(red, True)
except KeyboardInterrupt:
    GPIO.cleanup()
