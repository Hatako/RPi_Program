"""
7/31 研究ノートP.13に書いた図のようにスライドバーを配置し,
     移動ロボットを操作することができるようにする

     直進, 回転, 停止ボタンを作成
"""

import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep

root = tk.Tk()
root.title("移動ロボットを動かそう!")
root.geometry("600x400")


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
#STATE = "停止"

print("please wait")
sleep(0.1)			
print("go")
p1.start(0)
p2.start(0)

# 前後左右バーを動かしたときの挙動
def State(event):
    degree1 = int(value1.get())
    degree2 = int(value2.get())
    right = 0
    left = 0
    if degree1 >= 0: # 前進状態
        GPIO.output(DIG1, GPIO.HIGH)
        GPIO.output(DIG2, GPIO.HIGH)
        if degree2 >= 0: # 右回転ぎみ
            right = degree1
            left = degree1+degree2
            p1.start(right)
            p2.start(left)
        else:            # 左回転ぎみ
            right = degree1+abs(degree2)
            left = degree1
            p1.start(right)
            p2.start(left)
        print("右: {0}   左: {1}".format(right, left))


    else: # 後進状態
        GPIO.output(DIG1, GPIO.LOW)
        GPIO.output(DIG2, GPIO.LOW)
        degree1 = abs(degree1)
        if degree2 >= 0: # 右回転ぎみ
            right = degree1
            left = degree1+degree2
            p1.start(right)
            p2.start(left)
        else:            # 左回転ぎみ
            right = degree1+abs(degree2)
            left = degree1
            p1.start(right)
            p2.start(left)
        print("左: {0}   右: {1}".format(-left, -right))


def Horizon0(event):
    degree1 = int(value1.get())
    if degree1>=0:
        GPIO.output(DIG1, GPIO.HIGH)
        GPIO.output(DIG2, GPIO.HIGH)
        p1.start(degree1)
        p2.start(degree1)
    else:
        GPIO.output(DIG1, GPIO.LOW)
        GPIO.output(DIG2, GPIO.LOW)
        p1.start(abs(degree1))
        p2.start(abs(degree1))
    value2.set(0)
    print("左: {0}   右: {1}".format(degree1, degree1))



def Stop(event):
    p1.start(0)
    p2.start(0)
    value1.set(0)
    value2.set(0)
#    print("左: 0   右: 0")


var1 = tk.DoubleVar()
value1 = tk.Scale(root, label='前後', length=300, tickinterval=10, orient='v', from_=50, to=-50, variable=var1, command=State)
value1.set(0)
value1.place(x=400, y=50)

var2 = tk.DoubleVar()
value2 = tk.Scale(root, label='左右', length=300, tickinterval=10, orient='h', from_=-50, to=50, variable=var2, command=State)
value2.set(0)
value2.place(x=50, y=150)

Button_horizontal0 = tk.Button(text="左右0にセット", width=10, height=4)
Button_horizontal0.bind("<Button-1>", Horizon0)
Button_horizontal0.place(x=100, y=250)

Button_stop = tk.Button(text="停止", width=10, height=4)
Button_stop.bind("<Button-1>", Stop)
Button_stop.place(x=200, y=250)


root.mainloop()