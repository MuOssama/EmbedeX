import RPi.GPIO as gpio
import time
led_pin = 4
#set BCM convention
gpio.setmode(gpio.BCM)

#set pin3 as output
gpio.setup(led_pin, gpio.OUT)


#set led pin pwm
pwmFreq = 100 #100 Hz which is 1/100 sec as T = 1/F
channel = gpio.PWM(led_pin, pwmFreq)
while True:
	for duty in range(0,101):
		channel.start(duty)
		print(F'Duty: {duty}')
		time.sleep(0.1)
	for duty in range(0,101):
		channel.start(100-duty)
		print(F'Duty: {100-duty}')
		time.sleep(0.05)

