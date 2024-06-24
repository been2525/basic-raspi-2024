# URL 접속을 /led/on, /led/off로 접속하면 led를 on, off하는 웹페이지를 만들자
from flask import Flask
import RPi.GPIO as GPIO

red = 16

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)

@app.route("/")				
def hello():
	return "Hello World!!"

@app.route("/led/<state>")
def led(state):
	if state == "on":
		GPIO.output(red, False)
		return "LED ON"
	elif state == "off":
		GPIO.output(red, True)
		return "LED OFF"
	elif state == "clear":
		GPIO.cleanup()
		return "GPIO Cleanup()"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="9090", debug=True)

