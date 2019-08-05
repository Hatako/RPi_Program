"""
8/3 ロボットアームを動かすスライダーを追加する
"""

from Adafruit_PCA9685 import PCA9685
import time
import tkinter

root = tkinter.Tk()
root.geometry("1000x300")

pwm = PCA9685(0x40)
pwm.set_pwm_freq(50)

pwm.set_pwm(0, 0, 308)
servo0_pwmvalue = tkinter.DoubleVar()
servo0_pwmvalue.set(308)


def control_servo0(event):
	servo0_pwmvalue_now = int(servo0_pwmvalue.get())
	pwm.set_pwm(0, 0, servo0_pwmvalue_now)
	print('サーボ0の角度: {}'.format(servo0_pwmvalue_now))

servo0 = tkinter.Scale(root, label='サーボモータ0', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=servo0_pwmvalue, command=control_servo0)
servo0.pack()

root.mainloop()

"""

#Tkオブジェクトのインスタンス作成
root = Tkinter.Tk()
root.geometry("400x400")
pwm = PWM(0x41) #インスタンス作成, I2cアドレス40番
pwm.setPWMFreq(50)  #周波数50Hzで動作(T=20ms)

servo0_value = Tkinter.DoubleVar()
pwm.setPWM(0,0,308)
servo0_value.set(308)


def Servo0(event):
	_ = int(PWM_VALUE0.get())
	pwm.setPWM(0,0,)
	print('サーボ1の角度: {}'.format(s0))

	

s0=Tkinter.Scale(root, label='サーボモータ1', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val0, command=controlServo0)
s0.pack()

root.mainloop()
"""