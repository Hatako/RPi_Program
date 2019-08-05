"""
8/3 ロボットアームを動かすスライダーを追加する
"""

from Adafruit_PWM_Servo_Driver import PWM
import time
import tkinter


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