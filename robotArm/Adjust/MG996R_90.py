#!/usr/bin/python
# -*- coding:utf-8 -*-
#MG996Rサーボモータの角度を90度に設定するファイル



from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x41) #インスタンス作成, I2cアドレス41番
pwm.setPWMFreq(50)  #周波数50Hzで動作(T=20ms)
servoMin = 100 # Min pulse length out of 4096
servoMax = 515   # Max pulse length out of 4096
servoMiddle=100+(servoMax+1-servoMin)/2
pwm.setPWM(15,0,servoMin) 
time.sleep(2)


def servo(inter, channel):#interのインターバルでchannelのサーボモータを動かす
	for i in range(servoMin,servoMiddle+1):
		pwm.setPWM(channel,0,i)	
		print(i)	
		time.sleep(inter)
servo(0.005,0)

#	time.sleep(1)
#	for i in range(servoMin,servoMax+1):
#		duty=servoMax+servoMin-i
#		pwm.setPWM(channel,0,duty)		
#		iRange=servoMax-servoMin
#		angle=180.0*(i-100)/iRange
#		print('angle: {0:.1f} [degree]'.format(angle))	
#		print(duty)
#		time.sleep(inter)
#	time.sleep(1)

