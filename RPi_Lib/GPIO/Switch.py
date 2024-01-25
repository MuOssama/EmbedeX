import RPi.GPIO as gpio
import time
ledPin = 5
switchPin = 6

gpio.setmode(gpio.BCM)

gpio.setup(ledPin, gpio.OUT)
gpio.setup(switchPin, gpio.IN, pull_up_down = gpio.PUD_UP)

while True:
	print(gpio.input(switchPin))
	if gpio.input(switchPin) == 0:
		gpio.output(ledPin, gpio.HIGH)
		print("Switch pressed");
		time.sleep(0.25)
		gpio.output(ledPin, gpio.LOW)
		
