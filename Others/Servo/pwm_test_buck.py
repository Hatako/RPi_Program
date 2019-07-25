#!/usr/bin/python
#このプログラムはサーボのスピード調整が可能です

from Adafruit_PWM_Servo_Driver import PWM
import time
pwm = PWM(0x40)
pwm.setPWMFreq(50)      
channel=input("Please Select Channel: ")
old_num=100
pwm.setPWM(channel,0,old_num)
print("Position Initialized!!")

def angle_spped(c, chara):
	print(chara)
	diff=new_num-old_num
	if diff>=0:
		inc=0
		while inc<=diff:
			pulse_now=old_num+inc
			print(pulse_now)
			pwm.setPWM(channel, 0, pulse_now)	
			time.sleep(0.001*c)
			inc+=1
	else:
		inc=0
		diff=-diff
		while inc<=diff:
			pulse_now=old_num-inc
			print(pulse_now)
			pwm.setPWM(channel, 0, pulse_now)	
			time.sleep(0.001*c)
			inc+=1
while True:
	new_num=input("Please Select Appropriate Number: 100~515:   ")
	if new_num<100 or new_num>515:
		print("Try again") 
		continue
	speed=input("Please Select Speed:       1  2  3:   " )
	if speed==1:
		angle_spped(10, "Slow")
	elif speed==2:
		angle_spped(5, "Norma;")
	elif speed==3:
		angle_spped(1, "Fast")
	else:
		print("Try again")
		continue
	old_num=new_num
