#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
H30 11/16
このプログラムは以下のサイトを参考にして作成しました
http://hira-hide.hatenablog.com/entry/20170423/1492939230
test01.pyとは少し違った処理方法をしています
XMLの解析を行い, 音声入力した単語と信頼度(CM)の抽出を行っています
OpenJtalkで喋らせるやつも入れてみました


H30 11/29
音声入力後の音声認識を一時停止するやつを試してみた--->成功!
"""


import socket
import xml.etree.ElementTree as ET
import subprocess
from datetime import datetime
#import commands
import time
import os


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


host = 'localhost'
port = 10500
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

	

print("a")
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
						print('スマートフォンと入力されました')
					elif command == u'リモコン':
						print('リモコンと入力されました')
					elif command == u'コップ':
						print('コップと入力されました')
					elif command == u'ペットボトル':
						print('ペットボトルと入力されました')
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
					print('scoreが0.99未満なので棄却')
					send_command('PAUSE')
					print('ちょいまち')
					time.sleep(10)
					print('おけ!')
					send_command('RESUME')
			data = ''
		else:
			data = data + client.recv(1024)
except KeyboardInterrupt:
	client.close()
















