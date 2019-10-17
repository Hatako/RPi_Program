#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
i=1
sleep=2

def talk(word):
	os.system('./AquesTalkPi ' + word + '| aplay')
	print(word)
	time.sleep(sleep)	

while i<=5:
	print( str(i)+ "回目")
	talk("おはよう")
	talk("こんにちは")
	talk("こんばんは")
	talk("おやすみ")
	talk("スマートフォン")
	talk("リモコン")
	i+=1
