import RPi.GPIO as GPIO
import time

piezoPin = 25
melody = [261, 293, 329, 369, 391, 440, 493, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
	while True:
		temp_val = input('1~8까지 범위입니다 > ')
		Buzz.start(50)
		if temp_val == '1':
			Buzz.ChangeFrequency(melody[int(temp_val) - 1])
			time.sleep(0.3)
		elif temp_val == '2':
			Buzz.ChangeFrequency(melody[int(temp_val) - 1])
			time.sleep(0.3)
		elif temp_val == '3':
			Buzz.ChangeFrequency(melody[int(temp_val) - 1])
			time.sleep(0.3)
		elif temp_val == '4':
			Buzz.ChangeFrequency(melody[int(temp_val) - 1])
			time.sleep(0.3)
		elif temp_val == '5':
			Buzz.ChangeFrequency(melody[int(temp_val) - 1])
			time.sleep(0.3)
		elif temp_val == '6':
			Buzz.ChangeFrequency(melody[int(temp_val) - 1])
			time.sleep(0.3)
		elif temp_val =='7':
			Buzz.ChangeFrequency(melody[int(temp_val) - 1])
			time.sleep(0.3)
		elif temp_val == '8':
			Buzz.ChangeFrequency(melody[int(temp_val) - 1])
			time.sleep(0.3)
		else:
			print('다시 입력해주세요')
		Buzz.stop()
except KeyboardInterrupt:
		GPIO.cleanup()
