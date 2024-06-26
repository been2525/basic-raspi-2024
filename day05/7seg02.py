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
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)

try:
    while True:
        if GPIO.input(switch) == True:
            if count == 0:
                #0
                GPIO.output(a,False)
                GPIO.output(b,False)
                GPIO.output(c,False)
                GPIO.output(d,False)
                GPIO.output(e,False)
                GPIO.output(f,False)
                GPIO.output(g,True)
                time.sleep(1)
                print(count)
                count = count + 1
            elif count == 1:
            #1
                GPIO.output(a,True)
                GPIO.output(b,False)
                GPIO.output(c,False)
                GPIO.output(d,True)
                GPIO.output(e,True)
                GPIO.output(f,True)
                GPIO.output(g,True)
                time.sleep(1)
                print(count)
                count = count + 1

            elif count == 2:
            #2
                GPIO.output(a,False)
                GPIO.output(b,False)
                GPIO.output(c,True)
                GPIO.output(d,False)
                GPIO.output(e,False)
                GPIO.output(f,True)
                GPIO.output(g,False)
                time.sleep(1)
                print(count)
                count = count + 1

            elif count == 3:
                #3
                GPIO.output(a,False)
                GPIO.output(b,False)
                GPIO.output(c,False)
                GPIO.output(d,False)
                GPIO.output(e,True)
                GPIO.output(f,True)
                GPIO.output(g,False)
                time.sleep(1)
                print(count)
                count = count + 1

            elif count == 4:
                #4
                GPIO.output(a,True)
                GPIO.output(b,False)
                GPIO.output(c,False)
                GPIO.output(d,True)
                GPIO.output(e,True)
                GPIO.output(f,False)
                GPIO.output(g,False)
                time.sleep(1)
                print(count)
                count = count + 1

            elif count == 5:
                #5        
                GPIO.output(a,False)
                GPIO.output(b,True)
                GPIO.output(c,False)
                GPIO.output(d,False)
                GPIO.output(e,True)
                GPIO.output(f,False)
                GPIO.output(g,False)
                time.sleep(1)
                print(count)
                count = count + 1

            elif count == 6:
                #6
                GPIO.output(a,False)
                GPIO.output(b,True)
                GPIO.output(c,False)
                GPIO.output(d,False)
                GPIO.output(e,False)
                GPIO.output(f,False)
                GPIO.output(g,False)
                time.sleep(1)
                print(count)
                count = count + 1

            elif count == 7:
                #7
                GPIO.output(a,False)
                GPIO.output(b,False)
                GPIO.output(c,False)
                GPIO.output(d,True)
                GPIO.output(e,True)
                GPIO.output(f,False)
                GPIO.output(g,True)
                time.sleep(1)
                print(count)
                count = count + 1

            elif count == 8:
                #8
                GPIO.output(a,False)
                GPIO.output(b,False)
                GPIO.output(c,False)
                GPIO.output(d,False)
                GPIO.output(e,False)
                GPIO.output(f,False)
                GPIO.output(g,False)
                time.sleep(1)
                print(count)
                count = count + 1

            elif count == 9:
                #9
                GPIO.output(a,False)
                GPIO.output(b,False)
                GPIO.output(c,False)
                GPIO.output(d,True)
                GPIO.output(e,True)
                GPIO.output(f,False)
                GPIO.output(g,False)
                time.sleep(1)
                print(count)
                count = 0
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