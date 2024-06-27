import RPi.GPIO as GPIO
import time

count = 0
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

def fndOut(data, sel):						
	for i in range(0,7):
		GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
		for j in range(0,2): # 자리수의 fnd만 on
			if j==sel:
				GPIO.output(fndSels[j], 0)
			else:
				GPIO.output(fndSels[j], 1)

try:
	while True:
		count += 1
		d1000 = count / 1000
		d100 = count % 1000 / 100
		d10 = count % 100 / 10
		d1 = count % 10

		d = [d1,d10,d100,d1000]
		
		for i in range(3, -1, -1):
			fndOut(int(d[i]), i)
			time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
