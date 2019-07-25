#!/usr/bin/python
# -*- coding:utf-8 -*-
#MG996Rサーボモータの角度を90度に設定するファイル



from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40) #インスタンス作成, I2cアドレス40番
pwm.setPWMFreq(50)  #周波数50Hzで動作(T=20ms)
servoMin = 100 # Min pulse length out of 4096
servoMax = 515   # Max pulse length out of 4096
servoMiddle=100+(servoMax+1-servoMin)/2
pwm.setPWM(15,0,servoMin) 
time.sleep(1)


def servo(inter, channel):#interのインターバルでchannelのサーボモータを動かす
	for i in range(servoMin,servoMiddle+1):
		pwm.setPWM(channel,0,i)	
		print("サーボ{0}: {1}".format(str(channel), str(i)))	
		time.sleep(inter)
		
servo(0.005,0)
servo(0.005,1)
servo(0.005,2)
servo(0.005,8)
servo(0.005,9)
servo(0.005,10)



