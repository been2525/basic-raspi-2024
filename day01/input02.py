import RPi.GPIO as GPIO
import time

red = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)


try:
	while True:
		temp_val = input(' > ')
		if temp_val == "o":
			GPIO.output(red, False)
		elif temp_val== "x":
			GPIO.output(red, True)


except KeyboardInterrupt:
		GPIO.cleanup()
