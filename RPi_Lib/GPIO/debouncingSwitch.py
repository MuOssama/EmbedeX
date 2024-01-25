import RPi.GPIO as gpio
import time
ledPin = 5
switchPin = 6

gpio.setmode(gpio.BCM)

gpio.setup(ledPin, gpio.OUT)
gpio.setup(switchPin, gpio.IN, pull_up_down = gpio.PUD_UP)

debounceTime=50/1000
def debounceRead(pin, dtime):
	switchState = gpio.input(pin)
	#assuming pull up resistor activated
	if switchState == 0:
		time.sleep(dtime) 
		switchState = gpio.input(pin)
		if switchState == 0:
			return gpio.input(switchPin)
while True:
	if debounceRead(switchPin, debounceTime) == 0:
		gpio.output(ledPin, gpio.HIGH)
		print("Switch pressed");
		time.sleep(0.25)
		gpio.output(ledPin, gpio.LOW)
		
