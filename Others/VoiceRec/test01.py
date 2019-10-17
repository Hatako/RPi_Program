# -*- coding: utf-8 -*-
#11/12(月)
#このプログラムはsocke通信を用いて指定のホスト, ポートのサーバからメッセージを受取り受け取ったメッセージに応じて個々の処理を行っています
#Juliusをモジュールモードで実行した際に, 以下のhost, portからメッセージを受信します


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
			print( message)
			if message == "":
				print('クライアントの実行を停止します')
				flag = False
				break
#			else:
#				if "WORD=\"こんにちは\"" in message:
#					print "Hello"
#				if "WORD=\"おはよう\"" in message:
#					print "Good morning"

client_socket.close()
