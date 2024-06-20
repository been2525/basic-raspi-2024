import RPi.GPIO as GPIO
import time

red = 21
blue = 26

#GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)
#GPIO핀 설정(입력/출력)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)



try:
	while True:
		GPIO.output(red, False)
		GPIO.output(blue, True)
		time.sleep(1)
		GPIO.output(red, True)
		GPIO.output(blue, False)

		time.sleep(1)
		GPIO.output(red, True)
		GPIO.output(blue, True)

		time.sleep(1)

except KeyboardInterrupt:  #Ctrl + c
		GPIO.cleanup()
