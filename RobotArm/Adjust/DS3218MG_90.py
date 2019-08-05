#!/usr/bin/python
# -*- coding:utf-8 -*-

#このプログラムはサーボモータDS3218MG用に作成されました
#サーボモータを90度に設定するファイルです

from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40) #インスタンス作成, I2cアドレス40番
pwm.setPWMFreq(50)  #周波数50Hzで動作(T=20ms)
servoMin = 92 # Min pulse is 0
servoMax = 302 # Max pulse length out of 4096
pwm.setPWM(0,0,servoMin) 
time.sleep(2)


def servo(inter, channel):#interのインターバルでchannelのサーボモータを動かす
	for i in range(servoMin,servoMax+1):
		pwm.setPWM(channel,0,i)		
		print(i)
#		iRange=servoMax-servoMin
#		angle=180.0*(i-100)/iRange
#		print('angle: {0:.1f} [degree]'.format(angle))	
		time.sleep(inter)
#	time.sleep(1)
#	pwm.setPWM(0,0,servoMin) 

servo(0.002,0)
