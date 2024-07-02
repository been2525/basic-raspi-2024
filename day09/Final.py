import sys
import time
from picamera2 import Picamera2
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QPushButton, QLCDNumber
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, pyqtSignal
import RPi.GPIO as GPIO
import datetime

class GPIOThread(QThread):
    update_display = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.running = False
        self.count = 0

        # GPIO 설정
        self.segment_pins = [26, 25, 20, 12, 13, 19, 16]
        self.digit_pins = [22, 17, 27, 4]
        self.led_pins = {'red': 21, 'green': 24, 'blue': 23}
        self.segment_patterns = [
            [False, False, False, False, False, True, True], # 0
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

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.picam2 = Picamera2()
        camera_config = self.picam2.create_preview_configuration()
        self.picam2.configure(camera_config)
        self.picam2.start()
        for pin in self.segment_pins:
            GPIO.setup(pin, GPIO.OUT)
        for pin in self.digit_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        for pin in self.led_pins.values():
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

    def display_number(self, number):
        digits = [int(d) for d in str(number).zfill(4)]
        for i in range(4):
            GPIO.output(self.digit_pins[i], GPIO.HIGH)
            pattern = self.segment_patterns[digits[i]]
            for pin, state in zip(self.segment_pins, pattern):
                GPIO.output(pin, state)
            time.sleep(0.005)  # 지연을 추가하여 숫자 표시 오류를 방지합니다.
            GPIO.output(self.digit_pins[i], GPIO.LOW)

    def run(self):
        while True:
            if self.running:
                self.count += 1
                self.update_display.emit(self.count)
                self.display_number(self.count)
                time.sleep(1)

    def start_counting(self):
        self.running = True

    def stop_counting(self):
        self.running = False

    def reset_count(self):
        self.count = 0

    def increment_count(self):
        self.count += 1
        self.update_display.emit(self.count)
        self.display_number(self.count)

    def control_led(self, color):
        if color == 'red':
            GPIO.output(self.led_pins['red'], False)
            GPIO.output(self.led_pins['blue'], True)
            GPIO.output(self.led_pins['green'], True)
        elif color == 'blue':
            GPIO.output(self.led_pins['red'], True)
            GPIO.output(self.led_pins['blue'], False)
            GPIO.output(self.led_pins['green'], True)
        elif color == 'green':
            GPIO.output(self.led_pins['red'], True)
            GPIO.output(self.led_pins['blue'], True)
            GPIO.output(self.led_pins['green'], False)
        elif color == 'off':
            GPIO.output(self.led_pins['red'], True)
            GPIO.output(self.led_pins['blue'], True)
            GPIO.output(self.led_pins['green'], True)

    def camera_on(self):
        now = datetime.datetime.now()
        print(now)
        fileName = now.strftime('%Y-%m-%d %H:%M:%S')
        self.picam2.capture_file(fileName + ".jpg")
        time.sleep(0.2)

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('count.ui', self)  # UI 파일을 로드합니다.

        # UI 요소를 설정합니다.
        self.startButton.clicked.connect(self.start_counting)
        self.stopButton.clicked.connect(self.stop_counting)
        self.countButton.clicked.connect(self.increment_count)
        self.RedButton.clicked.connect(lambda: self.control_led('red'))
        self.GreenButton.clicked.connect(lambda: self.control_led('green'))
        self.BlueButton.clicked.connect(lambda: self.control_led('blue'))
        self.OffButton.clicked.connect(lambda: self.control_led('off'))
        self.CameraButton.clicked.connect(self.camera_on)

        self.gpio_thread = GPIOThread()
        self.gpio_thread.update_display.connect(self.update_lcd)
        self.gpio_thread.start()

    def start_counting(self):
        self.gpio_thread.start_counting()

    def stop_counting(self):
        self.gpio_thread.stop_counting()

    def increment_count(self):
        self.gpio_thread.increment_count()

    def control_led(self, color):
        self.gpio_thread.control_led(color)

    def camera_on(self):
        self.gpio_thread.camera_on()

    def update_lcd(self, value):
        self.lcdNumber.display(value)

    def closeEvent(self, event):
        self.gpio_thread.stop_counting()
        self.gpio_thread.quit()
        self.gpio_thread.wait()
        GPIO.cleanup()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
