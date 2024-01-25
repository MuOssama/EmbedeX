import RPi.GPIO as gpio
import time
led_pin = 5
#set BCM convention
gpio.setmode(gpio.BCM)

#set pin3 as output
gpio.setup(led_pin, gpio.OUT)

#set led pin high and low with delay
while True:
	gpio.output(led_pin, gpio.HIGH)
	time.sleep(1)
	gpio.output(led_pin, gpio.LOW)
	time.sleep(1)
