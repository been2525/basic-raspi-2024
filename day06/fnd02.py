import RPi.GPIO as GPIO
import time

fndSegs = [26, 25, 20, 12, 13, 19, 16]
fndSels = [22, 17, 27, 4]
switch = 18  
fndDatas = [0x40, 0x79, 0x24, 0x30, 0x19, 0x12, 0x02, 0x78, 0x00, 0x10]

GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSegs, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut(data):						
	for i in range(0,7):
		GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))

try:
	while True:
		for i in range(0,1):
			GPIO.output(fndSels[i], 1)
#			GPIO.output(25, 0)
#			GPIO.output(20, 0)
			for j in range(0,10):
				fndOut(j)
				time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
