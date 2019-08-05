# -*- coding: utf-8 -*-
#11/12(月)
#音声認識で物体を取得するプログラムです
#今のところペットボトル, リモコン, スマートフォン, コップの持ち上げのみで, ハサミ, ホッチキス, 消しゴム, 鉛筆, ボールペンはダミー


#11/29(木)
#RA動作中は音声認識停止

from Adafruit_PWM_Servo_Driver import PWM
import time
from collections import OrderedDict
import socket
import sys
import select
import os
import subprocess
import time
import xml.etree.ElementTree as ET


# OpenJtalkで好きな言葉を喋らせる
def jtalk(t):
	open_jtalk=['open_jtalk']
	mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
	htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
	speed=['-r','1.0']
	outwav=['-ow','open_jtalk.wav']
	cmd=open_jtalk+mech+htsvoice+speed+outwav
	c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
	c.stdin.write(t)
	c.stdin.close()
	c.wait()
	aplay = ['aplay','-q','open_jtalk.wav']
	wr = subprocess.Popen(aplay)


#---------------------------サーボモータ制御プログラム---------------------------------------------
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


#-----------------------Socket通信を行いメッセージの内容によってプログラムを動作させる------------------------------------
import socket
import sys
import select
import os
import subprocess
import time

host = "127.0.0.1"
port = 10500
bufsize = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))



#pause等の命令を送信
def send_command(command):
	msgbytes=command.encode('utf-8')+b'\n'
	client.sendall(msgbytes)
	print(msgbytes)
	

try:
	data = ''
	while 1:
		if '</RECOGOUT>\n.' in data:
			root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
			for whypo in root.findall('./SHYPO/WHYPO'):
				command = whypo.get('WORD')
				score = float(whypo.get('CM'))
				if score>=0.99:
					if command == u'スマートフォン':
						send_command('PAUSE')
						print "スマートフォンを取ります"
						jtalk("スマートフォンを取ります")
						print("しばらくお待ち下さい...........")
						angleList=[[308, 236, 513, 276, 140], [308, 293, 515, 458, 250], [308, 324, 515, 458, 250],[308, 293, 515, 458, 180]]
						for  i in angleList:
							[s1next, s2next, s3next, s4next, s5next]=i
							AllServoMove()
							[s1now, s2now, s3now, s4now, s5now]=[s1next, s2next, s3next, s4next, s5next]
							time.sleep(1)
						[s1next, s2next, s3next, s4next, s5next]=[s1ini, s2ini, s3ini, s4ini, s5ini]
						End()
						[s1now, s2now, s3now, s4now, s5now]=[308, 457, 515, 460, 140]
						print("動作完了!")
						send_command('RESUME')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
					elif command == u'リモコン':
						send_command('PAUSE')
						print "リモコンを取ります"
						jtalk("リモコンを取ります")
						print("しばらくお待ち下さい...........")
						angleList=[[308, 236, 513, 276, 140], [308, 301, 515, 460, 275], [308, 345, 515, 460, 275],[308, 301, 515, 460, 180]]
						for  i in angleList:
							[s1next, s2next, s3next, s4next, s5next]=i
							AllServoMove()
							[s1now, s2now, s3now, s4now, s5now]=[s1next, s2next, s3next, s4next, s5next]
							time.sleep(1)
						[s1next, s2next, s3next, s4next, s5next]=[s1ini, s2ini, s3ini, s4ini, s5ini]
						End()
						[s1now, s2now, s3now, s4now, s5now]=[308, 457, 515, 460, 140]
						print("動作完了!")
						send_command('RESUME')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
					elif command == u'コップ':
						send_command('PAUSE')
						print "コップを取ります"
						jtalk("コップを取ります")
						print("しばらくお待ち下さい...........")
						angleList=[[308, 236, 513, 276, 140], [308, 200,  490, 270, 252], [308, 233, 490, 270, 252],[308, 200, 490, 270, 180]]
						for  i in angleList:
							[s1next, s2next, s3next, s4next, s5next]=i
							AllServoMove()
							[s1now, s2now, s3now, s4now, s5now]=[s1next, s2next, s3next, s4next, s5next]
							time.sleep(1)
						[s1next, s2next, s3next, s4next, s5next]=[s1ini, s2ini, s3ini, s4ini, s5ini]
						End()
						[s1now, s2now, s3now, s4now, s5now]=[308, 457, 515, 460, 140]
						print("動作完了!")
						send_command('RESUME')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
					elif command == u'ペットボトル':
						send_command('PAUSE')
						print"ペットボトルを取ります"
						jtalk("ペットボトルを取ります")
						print("しばらくお待ち下さい...........")
						angleList=[[308, 236, 513, 276, 140], [308, 236, 513, 276, 280], [308, 236, 490, 250, 280],[308, 236, 513, 276, 180]]
						for  i in angleList:
							[s1next, s2next, s3next, s4next, s5next]=i
							AllServoMove()
							[s1now, s2now, s3now, s4now, s5now]=[s1next, s2next, s3next, s4next, s5next]
							time.sleep(1)
						[s1next, s2next, s3next, s4next, s5next]=[s1ini, s2ini, s3ini, s4ini, s5ini]
						End()
						[s1now, s2now, s3now, s4now, s5now]=[308, 457, 515, 460, 140]
						print("動作完了!")
						send_command('RESUME')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------						
					elif command == u'ハサミ':
						print('ハサミと入力されました')
					elif command == u'ホッチキス':
						print('ホッチキスと入力されました')
					elif command == u'消しゴム':
						print('消しゴムと入力されました')
					elif command == u'鉛筆':
						print('鉛筆と入力されました')
					elif command == u'ボールペン':
						print('ボールペンと入力されました')
				else:
					print("CMが0.99未満です")
			data = ''
		else:
			data = data + client.recv(1024)
					
					
except KeyboardInterrupt:
	client.close()

