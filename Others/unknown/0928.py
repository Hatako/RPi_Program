# -*- coding: utf-8 -*-

import socket
import sys
import select
import os
import subprocess
import time

host = "127.0.0.1"
port = 10500
bufsize = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
	inputready, outputready, exceptrdy = select.select([client_socket], [],[])
	for s in inputready:
		if s == client_socket:
			message = client_socket.recv(bufsize)
#			print "受信したメッセージ : " + message
			if message == "":
				print 'クライアントの実行を停止します'
				flag = False
				break
			else:
				if "WORD=\"こんにちは\"" in message:
					print "こんにちは"
					os.system('./aquestalkpi/AquesTalkPi '+ 'こんにちは' + '| aplay')
				if "WORD=\"おはよう\"" in message:
					print "おはよう"
					os.system('./aquestalkpi/AquesTalkPi '+ 'おはようございます' + '| aplay')
				if "WORD=\"おやすみ\"" in message:
					print "おやすみ"
					os.system('./aquestalkpi/AquesTalkPi '+ 'おやすみなさい' + '| aplay')
				if "WORD=\"さようなら\"" in message:
					print "さようなら"
					os.system('./aquestalkpi/AquesTalkPi '+ 'さようなら' + '| aplay')
				if "WORD=\"テレビ\"" in message:
					print "テレビ"
					os.system('./aquestalkpi/AquesTalkPi '+ 'テレビが見たいんですね' + '| aplay')
				if "WORD=\"スマートフォン\"" in message:
					print "スマートフォン"
					os.system('./aquestalkpi/AquesTalkPi '+ 'スマートフォンを探します' + '| aplay')
				if "WORD=\"飲み物\"" in message:
					print "飲み物"
					os.system('./aquestalkpi/AquesTalkPi '+ '飲み物を取りに行きますね' + '| aplay')
				if "WORD=\"リモコン\"" in message:
					print "リモコン"
					os.system('./aquestalkpi/AquesTalkPi '+ 'リモコンを取りに行きますね' + '| aplay')
				if "WORD=\"ティッシュ\"" in message:
					print "ティッシュ"
					os.system('./aquestalkpi/AquesTalkPi '+ 'ティッシュを取りに行きますね' + '| aplay')
client_socket.close()
