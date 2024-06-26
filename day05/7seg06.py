import RPi.GPIO as GPIO
import time

segment_pins = [26,25,20,12,13,19,16]
digit_pins = [22,17,27,4]

segment_patterns = [
  [False, False, False, False, False, True, True], #0
  [True, False, False, True, True, True, True], #1
  [False, False, True, False, False, True, False], #2
  [False, False, False, False, True, True, False], #3
  [True, False, False, True, True, False, False], #4
  [False, True, False, False, True, False, False], #5
  [False, True, False, False, False, False, False], #6
  [False, False, False, True, True, True, True], #7
  [False, False, False, False, False, False, False], #8
  [False, False, False, False, True, False, False] 
]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in segment_pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in digit_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)  

def display_number(number):
    digits = [int(d) for d in str(number).zfill(4)] 
    for i in range(4):
        GPIO.output(digit_pins[i], GPIO.HIGH) 
        pattern = segment_patterns[digits[i]]
        for pin, state in zip(segment_pins, pattern):
            GPIO.output(pin, state)
        time.sleep(0.005) 
        GPIO.output(digit_pins[i], GPIO.LOW)  
def main():
    setup()
    try:
        for number in range(1, 10000):
            start_time = time.time()
            while time.time() - start_time < 0.5: 
                display_number(number)
    except KeyboardInterrupt:
        print("")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()