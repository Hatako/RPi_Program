#coding:utf-8
#このプログラムはGUIを用いてサーボモータを動かすプログラムです

from Adafruit_PWM_Servo_Driver import PWM
import time
import Tkinter 

#Tkオブジェクトのインスタンス作成
root=Tkinter.Tk()
root.geometry("400x300")
pwm_val=Tkinter.DoubleVar()
pwm_val.set(308)
pwm = PWM(0x40) #インスタンス作成, I2cアドレス40番
pwm.setPWMFreq(50)  #周波数50Hzで動作(T=20ms)

def controlServo(dc):
	pwm.setPWM(0,0,int(pwm_val.get()))
	print(int(pwm_val.get()))
s=Tkinter.Scale(root, label='LED', orient='h', from_=100, to=515, variable=pwm_val, command=controlServo)

s.pack()
root.mainloop()
