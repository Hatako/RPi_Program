#coding:utf-8
#H30 11/12 (沖縄支所講演会用プログラム)
#このプログラムはGUIを用いて5つのサーボモータを動かすプログラムです
#DSサーボが故障したのでMG996Rをとりあえず一番下で動作させています


from Adafruit_PWM_Servo_Driver import PWM
import time
import Tkinter 

#Tkオブジェクトのインスタンス作成
root=Tkinter.Tk()
root.geometry("1920x1080")
pwm = PWM(0x41) #インスタンス作成, I2cアドレス40番
pwm.setPWMFreq(50)  #周波数50Hzで動作(T=20ms)

pwm_val0=Tkinter.DoubleVar()
pwm.setPWM(0,0,308)
pwm_val0.set(308)
def controlServo0(dc):
	s0=int(pwm_val0.get())
	pwm.setPWM(0,0,s0)
	print('サーボ1の角度: {}'.format(s0))

pwm_val1=Tkinter.DoubleVar()
pwm.setPWM(1,0,308)
pwm_val1.set(308)
def controlServo1(dc):
	s1=int(pwm_val1.get())
	pwm.setPWM(1,0,s1)
	print('サーボ2の角度: {}'.format(s1))
	
pwm_val2=Tkinter.DoubleVar()
pwm.setPWM(2,0,308)
pwm_val2.set(308)
def controlServo2(dc):
	s2=int(pwm_val2.get())
	pwm.setPWM(2,0,s2)
	print('サーボ3の角度: {}'.format(s2))
	
	
pwm_val3=Tkinter.DoubleVar()
pwm.setPWM(8,0,308)
pwm_val3.set(308)
def controlServo3(dc):
	s3=int(pwm_val3.get())
	pwm.setPWM(8,0,s3)
	print('サーボ4の角度: {}'.format(s3))
	
	
pwm_val4=Tkinter.DoubleVar()
pwm.setPWM(9,0,140)
pwm_val4.set(140)
def controlServo4(dc):
	s4=int(pwm_val4.get())
	pwm.setPWM(9,0,s4)
	print('サーボ5の角度: {}'.format(s4))


s0=Tkinter.Scale(root, label='サーボモータ1', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val0, command=controlServo0)
s1=Tkinter.Scale(root, label='サーボモータ2',  length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val1, command=controlServo1)
s2=Tkinter.Scale(root, label='サーボモータ3', length=1900, tickinterval=10, orient='h', from_=100, to=515, variable=pwm_val2, command=controlServo2)
s3=Tkinter.Scale(root, label='サーボモータ4', length=1900, tickinterval=10, orient='h', from_=235, to=460, variable=pwm_val3, command=controlServo3)
s4=Tkinter.Scale(root, label='サーボモータ5', length=1900, tickinterval=10, orient='h', from_=140, to=300, variable=pwm_val4, command=controlServo4)

s0.pack()
s1.pack()
s2.pack()
s3.pack()
s4.pack()


root.mainloop()
