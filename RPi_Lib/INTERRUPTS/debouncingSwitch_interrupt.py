import RPi.GPIO as gpio
import time
ledPin = 5
switchPin = 6

gpio.setmode(gpio.BCM)

gpio.setup(ledPin, gpio.OUT)
gpio.setup(switchPin, gpio.IN, pull_up_down = gpio.PUD_UP)

debounceTime=50/1000
def Blink(switchPin):
	print("interrupt happened")
	switchState = gpio.input(switchPin)
	#assuming pull up resistor activated
	if switchState == 0:
		time.sleep(debounceTime) 
		switchState = gpio.input(switchPin)
		if switchState == 0:
			print("Switch pressed")
			gpio.output(ledPin, gpio.HIGH)
			time.sleep(0.25)
			gpio.output(ledPin, gpio.LOW)
			
#setup the interrupt
gpio.add_event_detect(switchPin, gpio.FALLING, callback=Blink)
while True:
	time.sleep(1000000000)
	
