#LEDのON, OFF, FLASHを試すプログラム



import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
		
def on():
	GPIO.output(21, True)

def off():
	GPIO.output(21, False)

def flash():
	i=0
	while i<10:
		GPIO.output(21, True)
		time.sleep(0.2)
		GPIO.output(21, False)
		time.sleep(0.2)
		i+=1
		print(i)

try:
	while 1:
		on()
		time.sleep(1)
		off()
		time.sleep(1)
		flash()
		time.sleep(1)
except KeyboardInterrupt:
	pass
GPIO.cleanup()

