import RPi.GPIO as GPIO
import time

switch = 6
red = 16
blue = 20
green = 21
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

try:
		while True:
			if count == 0:
				if GPIO.input(switch) == True:
					print("Pushed")
					GPIO.output(red, False)
					GPIO.output(blue, True)
					GPIO.output(green, True)
					time.sleep(0.3)
					count=1

				else:
					GPIO.output(red, True)
					GPIO.output(blue, True)
					GPIO.output(green, True)
			if count == 1:
				if GPIO.input(switch) == True:
					print("Pushed")
					GPIO.output(red, True)
					GPIO.output(blue, False)
					GPIO.output(green, True)
					time.sleep(0.3)
					count=2

				else:
					GPIO.output(red, True)
					GPIO.output(blue, True)
					GPIO.output(green, True)
			if count == 2:
				if GPIO.input(switch) == True:
					print("Pushed")
					GPIO.output(red, True)
					GPIO.output(blue, True)
					GPIO.output(green, False)
					time.sleep(0.3)
					count=0

				else:
					GPIO.output(red, True)
					GPIO.output(blue, True)
					GPIO.output(green, True)
except KeyboardInterrupt:
		GPIO.cleanup()
