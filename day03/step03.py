import RPi.GPIO as GPIO
import time

steps = [12, 13, 19, 26]
GPIO.setmode(GPIO.BCM)

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)

seq = [[0,0,0,1], [0,0,1,0],[0,1,0,0],[1,0,0,0]]

try:
	while 1:
		for stepPin in range(0, 4):
			moter = steps[stepPin]
			time.sleep(0.01)


except KeyboardInterrupt:
	GPIO.cleanup()
