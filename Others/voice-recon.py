# -*- coding: utf-8 -*-

import socket
import sys
import select
import os
import subprocess
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
def on():
	GPIO.output(21, True)

def off():
	GPIO.output(21, False)

def flash():
	i=0
	while i<3:
			GPIO.output(21, True)
			time.sleep(0.2)
			GPIO.output(21, False)
			time.sleep(0.2)
			i+=1

host = "127.0.0.1"
port = 10500
bufsize = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

try:
	while True:
		inputready, outputready, exceptrdy = select.select([client_socket], [],[])
		for s in inputready:
			if s == client_socket:
				message = client_socket.recv(bufsize)
#				print "受信したメッセージ : " + message
				if message == "":
					print 'クライアントの実行を停止します'
					flag = False
					break
				else:
					if "WORD=\"点灯\"" in message:
						on()
						print "点灯モードです"

					if "WORD=\"点滅\"" in message:
						print "点滅モードです"
						flash()

					if "WORD=\"消灯\"" in message:
						off()
						print"消灯モードです"
except KeyboardInterrupt:
	pass
client_socket.close()
GPIO.cleanup()
