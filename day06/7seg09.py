import RPi.GPIO as GPIO
import time

segment_pins = [26, 25, 20, 12, 13, 19, 16]
digit_pins = [22, 17, 27, 4]
switch = 18  

segment_patterns = [
    [False, False, False, False, False, False, True], # 0
    [True, False, False, True, True, True, True],    # 1
    [False, False, True, False, False, True, False], # 2
    [False, False, False, False, True, True, False], # 3
    [True, False, False, True, True, False, False],  # 4
    [False, True, False, False, True, False, False], # 5
    [False, True, False, False, False, False, False],# 6
    [False, False, False, True, True, True, True],   # 7
    [False, False, False, False, False, False, False],# 8
    [False, False, False, False, True, False, False] # 9
]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 스위치 핀 설정
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
        time.sleep(0.002)  # 지연 시간을 줄여 빠르게 변경
        GPIO.output(digit_pins[i], GPIO.LOW)

def main():
    setup()
    count = 0
    last_switch_state = GPIO.LOW

    try:
        while True:
            current_switch_state = GPIO.input(switch)
            if current_switch_state == GPIO.HIGH and last_switch_state == GPIO.LOW:
                count += 1
                display_number(count)
                time.sleep(0.2)  # 디바운스를 위해 약간의 지연 추가
            last_switch_state = current_switch_state
            display_number(count)
            time.sleep(0.01)  # 디스플레이 업데이트 간의 짧은 지연

    except KeyboardInterrupt:
        print("")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
