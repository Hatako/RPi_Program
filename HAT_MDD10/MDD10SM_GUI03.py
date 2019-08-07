"""
8/6 ロボットアームの各サーボモータを動かすスライダーを追加する(Servo0~Servo3)
8/7 物体を拾うボタンと持ち上げるボタンを作成する-->完
"""

from Adafruit_PCA9685 import PCA9685
import time
import tkinter as tk

root = tk.Tk()
root.geometry("1000x1000")
pwm = PCA9685(0x40)
pwm.set_pwm_freq(50)

pwm.set_pwm(0, 0, 395)
pwm.set_pwm(1, 0, 340)
pwm.set_pwm(2, 0, 240)
pwm.set_pwm(4, 0, 200)

servo0_pwmvalue = tk.DoubleVar()
servo1_pwmvalue = tk.DoubleVar()
servo2_pwmvalue = tk.DoubleVar()
servo3_pwmvalue = tk.DoubleVar()
servo0_pwmvalue.set(395)
servo1_pwmvalue.set(340)
servo2_pwmvalue.set(240)
servo3_pwmvalue.set(200)

def control_servo0(event):
	servo0_pwmvalue_now = int(servo0_pwmvalue.get())
	pwm.set_pwm(0, 0, servo0_pwmvalue_now)
	print('サーボ0の角度: {}'.format(servo0_pwmvalue_now))

def control_servo1(event):
	servo1_pwmvalue_now = int(servo1_pwmvalue.get())
	pwm.set_pwm(1, 0, servo1_pwmvalue_now)
	print('サーボ1の角度: {}'.format(servo1_pwmvalue_now))

def control_servo2(event):
	servo2_pwmvalue_now = int(servo2_pwmvalue.get())
	pwm.set_pwm(2, 0, servo2_pwmvalue_now)
	print('サーボ2の角度: {}'.format(servo2_pwmvalue_now))

def control_servo3(event):
	servo3_pwmvalue_now = int(servo3_pwmvalue.get())
	pwm.set_pwm(4, 0, servo3_pwmvalue_now)
	print('サーボ3の角度: {}'.format(servo3_pwmvalue_now))

def get(event):
    pwm.set_pwm(0, 0, 448)
    pwm.set_pwm(1, 0, 340)
    pwm.set_pwm(2, 0, 383)
    pwm.set_pwm(4, 0, 200)
    servo0_pwmvalue.set(448)
    servo1_pwmvalue.set(340)
    servo2_pwmvalue.set(383)
    servo3_pwmvalue.set(200)



def lift(event):
    pwm.set_pwm(0, 0, 448)
    pwm.set_pwm(1, 0, 340)
    pwm.set_pwm(2, 0, 383)
    pwm.set_pwm(4, 0, 200)
    servo0_pwmvalue.set(448)
    servo1_pwmvalue.set(340)
    servo2_pwmvalue.set(383)
    servo3_pwmvalue.set(200)


servo0 = tk.Scale(root, label='サーボモータ0', length=1900, tickinterval=10, orient='h', from_=395, to=560, variable=servo0_pwmvalue, command=control_servo0)
servo1 = tk.Scale(root, label='サーボモータ1', length=1900, tickinterval=10, orient='h', from_=340, to=560, variable=servo1_pwmvalue, command=control_servo1)
servo2 = tk.Scale(root, label='サーボモータ2', length=1900, tickinterval=10, orient='h', from_=240, to=415, variable=servo2_pwmvalue, command=control_servo2)
servo3 = tk.Scale(root, label='サーボモータ3', length=1900, tickinterval=10, orient='h', from_=200, to=400, variable=servo3_pwmvalue, command=control_servo3)

servo0.pack()
servo1.pack()
servo2.pack()
servo3.pack()

Button_get = tk.Button(text="拾う", width=10, height=4)
Button_get.bind("<Button-1>", get)
Button_get.pack()

Button_lift = tk.Button(text="持ち上げる", width=10, height=4)
Button_lift.bind("<Button-1>", lift)
Button_lift.pack()

root.mainloop()