import serial 
import time
UART = serial.Serial('/dev/serial0', 115200, timeout=1)
num=0
while True:
	if UART.isOpen():
		num = num + 1
		UART.write(str(num).encode('utf-8'))
		print(f"raspberryPy sent {num}")
		try:
			readingData = UART.readline().decode('utf-8')
			print(f"raspberryPi recived: {readingData}")
		except:
			print("empty Buffer")
		time.sleep(1)

		
