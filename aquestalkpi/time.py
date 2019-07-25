#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime


def talk(word, sleep):
	os.system('./AquesTalkPi ' + word + '| aplay')
	print(word)
	time.sleep(sleep)

while True:
	now=datetime.now()
	hour=now.hour
	minute=now.minute
	second=now.second
	time.sleep(1)
	print(second)
	if minute==0:
		talk("ぴ", 0.8)
		talk("ぴ", 0.8)
		talk("ぴ", 0.8)
		talk("ぴーーーー", 1)
		talk("現在の時刻は"+str(hour)+"時です",0)
		talk("ちなみにサッカー日本代表戦は明日夜23時から始まります",0)
		print("現在の時刻は"+str(hour)+"時です")
		time.sleep(100)
