from picamera2 import Picamera2
#from gpiozero import Button
import RPi.GPIO as GPIO
import time
import datetime

switch = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)



picam2 = Picamera2()
camera_config=picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

try:
	while True:
		if GPIO.input(switch) == True:
			now = datetime.datetime.now()
			print(now)
			fileName = now.strftime('%Y-%m-%d %H:%M:%S')
			picam2.capture_file(fileName + ".jpg")

			time.sleep(0.2)

except KeyboardInterrupt:
	pass
