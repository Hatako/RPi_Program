#coding:utf-8
#H30 11/10(沖縄支所講演会用プログラム)
#このプログラムはGUIを用いて1つのサーボモータを動かすプログラムです

from Adafruit_PWM_Servo_Driver import PWM
import time
import Tkinter 

#Tkオブジェクトのインスタンス作成
root=Tkinter.Tk()
root.geometry("1920x1080")
pwm = PWM(0x41) #インスタンス作成, I2cアドレス40番
pwm.setPWMFreq(50)  #周波数50Hzで動作(T=20ms)

pwm_val0=Tkinter.DoubleVar()
pwm_val0.set(308)
def controlServo0(dc):
	s0=int(pwm_val0.get())
	pwm.setPWM(0,0,s0)
	print('サーボ0の角度: {}'.format(s0))
	
	
pwm_val1=Tkinter.DoubleVar()
pwm_val1.set(308)
def controlServo1(dc):
	s1=int(pwm_val1.get())
	pwm.setPWM(1,0,s1)
	print('サーボ1の角度: {}'.format(s1))

s0=Tkinter.Scale(root, label='サーボモータ0', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val0, command=controlServo0)
s1=Tkinter.Scale(root, label='サーボモータ1', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val1, command=controlServo1)
s0.pack()
s1.pack()
root.mainloop()
