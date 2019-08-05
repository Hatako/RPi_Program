#!/usr/bin/python
# -*- coding:utf-8 -*-
#11/12(月) このプログラムは5サーボRAを用いて物体を持ち上げる用のプログラムです
#まずはじめに全サーボモータを初期位置に合わせ, そこから動作を開始させます
#またプログラムが終了すると自動的にロボットアームが初期位置に戻るようにします
#KeyboardInterruptの部分がまだ不十分
#同時処理ができないものか.....

from Adafruit_PWM_Servo_Driver import PWM
import time
from collections import OrderedDict

pwm = PWM(0x41) #インスタンス作成, I2cアドレス41番
pwm.setPWMFreq(50)  #周波数50Hzで動作(T=20ms)
[s1ini, s2ini, s3ini, s4ini, s5ini]=[308, 457, 515, 460, 140]
[s1now, s2now, s3now, s4now, s5now]=[308, 457, 515, 460, 140]
#サーボの番号(PiHAT上)と各サーボの初期位置を定義して, def Initial()で初期位置に設定
od=OrderedDict()
od["0"]=308
od["1"]=457
od["2"]=515
od["8"]=460
od["9"]=140

def Initial():
	for key, val in od.items():
		pwm.setPWM(int(key),0,val) 

#now:現在のサーボモータ位置, next次のサーボモータ位置
#どれだけモータを動かすか指示を与えている
def ServoControl(inter, channel, now, next):
	if next-now>0:
		servoMove=range(now, next+1)
		for i in servoMove:
			pwm.setPWM(channel, 0, i)	
			time.sleep(inter)
	elif next-now<0:
		servoMove=range(next, now+1)
		for i in reversed(servoMove):
			pwm.setPWM(channel, 0, i)
			time.sleep(inter)
	else:
		pass


# ServoControl関数を用いて全てのサーボモータを次の目標値に動かせる
def AllServoMove():
	ServoControl(0.005, 8, s4now, s4next)
	ServoControl(0.005,0, s1now, s1next)
	ServoControl(0.005, 1, s2now, s2next)
	ServoControl(0.005, 2, s3now, s3next)
	ServoControl(0.01, 9, s5now, s5next)
	time.sleep(1)
	
def End():
	ServoControl(0.005, 0, s1now, s1next)
	ServoControl(0.005, 1, s2now, s2next)
	ServoControl(0.005, 2, s3now, s3next)
	ServoControl(0.005, 8, s4now, s4next)
	ServoControl(0.005, 9, s5now, s5next)


#ペットボトルを取得する部分
angleList=[[308, 236, 513, 276, 140], [308, 236, 513, 276, 280], [308, 236, 490, 250, 280],[308, 236, 513, 276, 180]]
for  i in angleList:
	[s1next, s2next, s3next, s4next, s5next]=i
	AllServoMove()
	[s1now, s2now, s3now, s4now, s5now]=[s1next, s2next, s3next, s4next, s5next]
	time.sleep(1)
[s1next, s2next, s3next, s4next, s5next]=[s1ini, s2ini, s3ini, s4ini, s5ini]
End()

