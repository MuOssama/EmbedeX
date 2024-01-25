import RPi.GPIO as gpio
import time
SSEG_CC =[0b00111111,0b00000110,0b01011011,0b01001111,0b01100110,0b01101101,0b01111101,0b00000111,0b01111111,0b01101111]
SSEG_CA =[~0b00111111,~0b00000110,~0b01011011,~0b01001111,~0b01100110,~0b01101101,~0b01111101,~0b00000111,~0b01111111,~0b01101111]
SS_leastPinNum = 5
SS_mostPinNum = 12

def GET_BIT(byte,bit):
	#this function gets the bit value
	return ((byte>>bit)&1)
	
def SS_display(leastPin, value, ssType = "CA"):
	#this function displays value on Comman Anode seven segment CASS
	if value >=0 and value<10:
		print(f"printing the number: {value}")
		for i in range(0,8):
			#looping from lsb to msb in the value wanted to be displayed
			if ssType == "CA":
				bit_value = GET_BIT(SSEG_CA[value],i)
			elif ssType == "CC":
				bit_value = GET_BIT(SSEG_CC[value],i)
			else:
				print("wrong seven segment type selected")

			if bit_value == 1:
				gpio.output(leastPin+i, gpio.HIGH)
			else:
			    gpio.output(leastPin+i, gpio.LOW)

	else:
		print("you entered wrong number")

#set numbering convention to BCM
gpio.setmode(gpio.BCM)

#Setting 8 pins from 4-11 as output
for i in range(SS_leastPinNum,SS_mostPinNum+1):
	gpio.setup(i, gpio.OUT)

while True:
	for i in range(0,10):
		SS_display(SS_leastPinNum, i, "CA")
		time.sleep(1)
		
