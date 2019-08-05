#coding:utf-8
#H30 11/8 (沖縄支所講演会用プログラム)
#このプログラムはGUIを用いて6つのサーボモータを動かすプログラムです
#1つのロボットアーム中で異なるサーボモータを用いていたり, 同じサーボモータでも特性の違いがある(偽物が混ざっているせいかも知れない)
#基本エンドエフェクタ以外のサーボモータはまず90度に設定しています
#サーボモータの制御にはServo/PWM Pi HATを用いており0~3番ピン, 及び8,9番ピンを用いることを奨励します(今使ってる)

from Adafruit_PWM_Servo_Driver import PWM
import time
import Tkinter 

#Tkオブジェクトのインスタンス作成
root=Tkinter.Tk()
root.geometry("1920x1080")
pwm = PWM(0x40) #インスタンス作成, I2cアドレス40番
pwm.setPWMFreq(50)  #周波数50Hzで動作(T=20ms)

pwm_val0=Tkinter.DoubleVar()
pwm_val0.set(308)
def controlServo0(dc):
	s0=int(pwm_val0.get())
	pwm.setPWM(0,0,s0)
	print('サーボ0の角度: {}'.format(s0))

pwm_val1=Tkinter.DoubleVar()
pwm_val1.set(302)
def controlServo1(dc):
	s1=int(pwm_val1.get())
	pwm.setPWM(1,0,s1)
	print('サーボ1の角度: {}'.format(s1))
	
pwm_val2=Tkinter.DoubleVar()
pwm_val2.set(308)
def controlServo2(dc):
	s2=int(pwm_val2.get())
	pwm.setPWM(2,0,s2)
	print('サーボ2の角度: {}'.format(s2))
	
	
pwm_val3=Tkinter.DoubleVar()
pwm_val3.set(308)
def controlServo3(dc):
	s3=int(pwm_val3.get())
	pwm.setPWM(8,0,s3)
	print('サーボ3の角度: {}'.format(s3))
	
	
pwm_val4=Tkinter.DoubleVar()
pwm_val4.set(308)
def controlServo4(dc):
	s4=int(pwm_val4.get())
	pwm.setPWM(9,0,s4)
	print('サーボ4の角度: {}'.format(s4))
	

pwm_val5=Tkinter.DoubleVar()
pwm_val5.set(138)
def controlServo5(dc):
	s5=int(pwm_val5.get())
	pwm.setPWM(10,0,s5)
	print('サーボ5の角度: {}'.format(s5))

s0=Tkinter.Scale(root, label='サーボモータ0', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val0, command=controlServo0)
s1=Tkinter.Scale(root, label='サーボモータ1',  length=1900, tickinterval=10, orient='h', from_=92, to=515, variable=pwm_val1, command=controlServo1)
s2=Tkinter.Scale(root, label='サーボモータ2', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val2, command=controlServo2)
s3=Tkinter.Scale(root, label='サーボモータ3', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val3, command=controlServo3)
s4=Tkinter.Scale(root, label='サーボモータ4', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val4, command=controlServo4)
s5=Tkinter.Scale(root, label='サーボモータ5',length=1900, tickinterval=10,  orient='h', from_=138, to=300, variable=pwm_val5, command=controlServo5)

s0.pack()
s1.pack()
s2.pack()
s3.pack()
s4.pack()
s5.pack()

root.mainloop()
