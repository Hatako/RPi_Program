#!/usr/bin/python
from Adafruit_PWM_Servo_Driver import PWM
import time
pwm = PWM(0x40)
pwm.setPWMFreq(50)      
pwm.setPWM(0,0,100)
pwm.setPWM(1,0,100)
time.sleep(1)
print("Initialized")

while True:
	pwm.setPWM(1,0,200)
	pwm.setPWM(0,0,300)
	time.sleep(1)
	pwm.setPWM(1,0,100)
	time.sleep(1.5)
	pwm.setPWM(1,0,200)
	pwm.setPWM(0,0,100)
	time.sleep(1)
	pwm.setPWM(1,0,100)
	time.sleep(1.5)
