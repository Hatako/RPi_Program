"""
7/30 GUI上で移動ロボットを動かすプログラムを作成する
具体的には前進, 後退, 左回転, 右回転, 停止のボタンを配置
また, 上部にスライドバーを配置し進んだり回転する速度を変化できるようにする
停止ボタンが押された際はスライドバーを0の位置に戻すことを忘れないように
"""

import RPi.GPIO as GPIO		
from time import sleep
import tkinter as tk


root = tk.Tk()
root.title("移動ロボットを動かそう!")
root.geometry("500x500")

# HAT MDD10の設定
GPIO.setmode(GPIO.BCM)			
GPIO.setwarnings(False)			# enable warning from GPIO
AN1 = 12				# set pwm1 pin on MD10-hat
AN2 = 13				# set pwm2 pin on MD10-Hat
DIG1 = 26				# set dir1 pin on MD10-Hat(右)
DIG2 = 24				# set dir2 pin on MD10-Hat(左)

GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
p1 = GPIO.PWM(AN1, 100)			# set pwm for M1
p2 = GPIO.PWM(AN2, 100)			# set pwm for M2

print("please wait")
#sleep(1)				# delay for 1 seconds
print("go")
p1.start(0)
p2.start(0)
#----------------------------------------------

button_forward = tk.Button(text="前進", width=4, height=2)
button_forward.place(x=200, y=100)
button_left = tk.Button(text="左回転", width=4, height=2)
button_left.place(x=100, y=200)
button_back = tk.Button(text="後退", width=4, height=2)
button_back.place(x=200, y=300)
button_right = tk.Button(text="右回転", width=4, height=2)
button_right.place(x=300, y=200)
button_stop = tk.Button(text="停止", width=4, height=2)
button_stop.place(x=200, y=200)
root.mainloop()

#def control(dc):
#	s0=int(pwm_val0.get())
#	pwm.setPWM(0,0,s0)
#	print('サーボ1の角度: {}'.format(s0))





#try:					
#  while True:

#   print ("前進")				# display "Forward" when programe run
#   GPIO.output(DIG1, GPIO.HIGH)		# set DIG1 as HIGH, M1B will turn ON
#   GPIO.output(DIG2, GPIO.HIGH)		# set DIG2 as HIGH, M2B will turn ON
#   p1.start(20)			# set speed for M1 at 100%
#   p2.start(20)			# set speed for M2 at 100%
#   sleep(5)				#delay for 2 second

#except:					# exit programe when keyboard interupt
#   p1.start(0)				# set speed to 0
#   p2.start(0)				# set speed to 0
#					# Control+x to save file and exit