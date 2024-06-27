import RPi.GPIO as GPIO
import time

fndSegs = [26, 25, 20, 12, 13, 19, 16]
fndSels = [22, 17, 27, 4]
switch = 18  

fndDatas = [
    [False, False, False, False, False, False, True], # 0 0x40
    [True, False, False, True, True, True, True],    # 1 0x79
    [False, False, True, False, False, True, False], # 2 0x24
    [False, False, False, False, True, True, False], # 3 0x30
    [True, False, False, True, True, False, False],  # 4 0x19
    [False, True, False, False, True, False, False], # 5 0x12
    [False, True, False, False, False, False, False], # 6 0x02
    [False, False, False, True, True, True, True],   # 7  0x78
    [False, False, False, False, False, False, False], # 0x00
    [False, False, False, False, True, False, False] # 9 0x10
]

GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
	GPIO.setup(fndSegs, GPIO.OUT)
	GPIO.output(fndSeg, 0)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 1)

def fndOut():						# 하나의 숫자형태를 만드는 함수
	for i in range(0,7):
		GPIO.output(fndSegs[i], fndDatas[1] & (0x01 << i))

try:
	while True:
		for i in range(0,1):
			GPIO.output(fndSels[i], 1)
#			GPIO.output(25, 0)
#			GPIO.output(20, 0)
			for j in range(0,10):
				fndOut(5)
				time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
