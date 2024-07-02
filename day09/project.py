import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, pyqtSignal
import RPi.GPIO as GPIO

class GPIOThread(QThread):
    update_display = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.running = False
        self.count = 0

        self.segment_pins = [26, 25, 20, 12, 13, 19, 16]
        self.digit_pins = [22, 17, 27, 4]
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
        for pin in self.segment_pins:
            GPIO.setup(pin, GPIO.OUT)
        for pin in self.digit_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def display_number(self, number):
        digits = [int(d) for d in str(number).zfill(4)]
        for i in range(4):
            GPIO.output(self.digit_pins[i], GPIO.HIGH)
            pattern = self.segment_patterns[digits[i]]
            for pin, state in zip(self.segment_pins, pattern):
                GPIO.output(pin, state)
            time.sleep(0.002)
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('./count.ui', self) 

        self.startButton.clicked.connect(self.start_counting)
        self.stopButton.clicked.connect(self.stop_counting)

        self.gpio_thread = GPIOThread()
        self.gpio_thread.start()

    def start_counting(self):
        self.gpio_thread.start_counting()

    def stop_counting(self):
        self.gpio_thread.stop_counting()

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
