import RPi.GPIO as GPIO
import time

switch = 18
a = 26
b = 25
c = 20
d = 12
e = 13
f = 19
g = 16
com4 = 4
count = 0
com1 = 22
com2 = 17
com3 = 27
i = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(com1, GPIO.OUT)
GPIO.setup(com2, GPIO.OUT)
GPIO.setup(com3, GPIO.OUT)
GPIO.setup(com4, GPIO.OUT)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)

def first():
        GPIO.output(com1,True)
        GPIO.output(a,True)
        GPIO.output(b,False)
        GPIO.output(c,False)
        GPIO.output(d,True)
        GPIO.output(e,True)
        GPIO.output(f,True)
        GPIO.output(g,True)

def second():
        GPIO.output(com2,True)
        GPIO.output(a,False)
        GPIO.output(b,False)
        GPIO.output(c,True)
        GPIO.output(d,False)
        GPIO.output(e,False)
        GPIO.output(f,True)
        GPIO.output(g,False)

def third():
        GPIO.output(com3,True)
        GPIO.output(a,False)
        GPIO.output(b,False)
        GPIO.output(c,False)
        GPIO.output(d,False)
        GPIO.output(e,True)
        GPIO.output(f,True)
        GPIO.output(g,False)             

def fourth():
        GPIO.output(com4,True)
        GPIO.output(a,True)
        GPIO.output(b,False)
        GPIO.output(c,False)
        GPIO.output(d,True)
        GPIO.output(e,True)
        GPIO.output(f,False)
        GPIO.output(g,False)

try:
    while True:
            first()
            second()
            third()
            fourth()
        #if GPIO.input(switch) == True:
            #for i in range(9):
        # GPIO.input(com1, True)
        # GPIO.output(a,True)
        # GPIO.output(b,False)
        # GPIO.output(c,False)
        # GPIO.output(d,True)
        # GPIO.output(e,True)
        # GPIO.output(f,True)
        # GPIO.output(g,True)

        # GPIO.input(com2, True)
        # GPIO.output(a,False)
        # GPIO.output(b,False)
        # GPIO.output(c,True)
        # GPIO.output(d,False)
        # GPIO.output(e,False)
        # GPIO.output(f,True)
        # GPIO.output(g,False)

        # GPIO.input(com3, True)
        # GPIO.output(a,False)
        # GPIO.output(b,False)
        # GPIO.output(c,False)
        # GPIO.output(d,False)
        # GPIO.output(e,True)
        # GPIO.output(f,True)
        # GPIO.output(g,False)

        # GPIO.input(com4, True)
        # GPIO.output(a,True)
        # GPIO.output(b,False)
        # GPIO.output(c,False)
        # GPIO.output(d,True)
        # GPIO.output(e,True)
        # GPIO.output(f,False)
        # GPIO.output(g,False)

        # else:
        #     GPIO.output(a,True)
        #     GPIO.output(b,True)
        #     GPIO.output(c,True)
        #     GPIO.output(d,True)
        #     GPIO.output(e,True)
        #     GPIO.output(f,True)
        #     GPIO.output(g,True)


except KeyboardInterrupt:
		GPIO.cleanup()
