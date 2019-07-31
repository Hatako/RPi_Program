"""
7/30 GUI上で移動ロボットを動かすプログラムを作成する
具体的には前進, 後退, 左回転, 右回転, 停止のボタンを配置
また, 上部にスライドバーを配置し進んだり回転する速度を変化できるようにする
停止ボタンが押された際はスライドバーを0の位置に戻すことを忘れないように


7/31 GUIのプログラムは完成したが, スマホ等で操作することを考えるとまだまだ操作性が悪いので改良する
"""

import RPi.GPIO as GPIO		
from time import sleep
import tkinter as tk


root = tk.Tk()
root.title("移動ロボットを動かそう!")
root.geometry("700x800")

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
STATE = "停止"

print("please wait")
sleep(0.1)				# delay for 1 seconds
print("go")
p1.start(0)
p2.start(0)

# DoubleVarの値に応じてDuty比を変化させる
def State(event):
    if STATE=="停止":
        value.set(0)
        label1.config(text="停止状態なので動かせません")
    else:
        speed = int(var.get())
        p1.start(speed)
        p2.start(speed)
        selection = "speed:{}".format(speed)
        label1.config(text=selection)

def Forward_Reset(event):
    label1.config(text="")
    if STATE=="前進":
        pass
    else:
        global STATE
        STATE="前進"
        speed = int(var.get())
        for i in range(speed):
            speed-=1
            p1.start(speed)
            p2.start(speed)
            sleep(0.02)
        value.set(0)
        GPIO.output(DIG1, GPIO.HIGH)
        GPIO.output(DIG2, GPIO.HIGH)
        label2.config(text=STATE)

def Left_Reset(event):
    label1.config(text="")
    if STATE=="左回転":
        pass
    else:
        global STATE
        STATE="左回転"
        speed = int(var.get())
        for i in range(speed):
            speed-=1
            p1.start(speed)
            p2.start(speed)
            sleep(0.02)
        value.set(0)
        GPIO.output(DIG1, GPIO.HIGH)
        GPIO.output(DIG2, GPIO.LOW)
        label2.config(text=STATE)

def Back_Reset(event):
    label1.config(text="")
    if STATE=="後進":
        pass
    else:
        global STATE
        STATE="後進"
        speed = int(var.get())
        for i in range(speed):
            speed-=1
            p1.start(speed)
            p2.start(speed)
            sleep(0.02)
        value.set(0)
        GPIO.output(DIG1, GPIO.LOW)
        GPIO.output(DIG2, GPIO.LOW)
        label2.config(text=STATE)

def Right_Reset(event):
    label1.config(text="")
    if STATE=="右回転":
        pass
    else:
        global STATE
        STATE="右回転"
        speed = int(var.get())
        for i in range(speed):
            speed-=1
            p1.start(speed)
            p2.start(speed)
            sleep(0.02)
        value.set(0)
        GPIO.output(DIG1, GPIO.LOW)
        GPIO.output(DIG2, GPIO.HIGH)
        label2.config(text=STATE)

def Stop_Reset(event):
    label1.config(text="")
    if STATE=="停止":
        pass
    else:
        global STATE
        STATE="停止"
        speed = int(var.get())
        for i in range(speed):
            speed-=1
            p1.start(speed)
            p2.start(speed)
            sleep(0.02)
        value.set(0)
        label2.config(text=STATE)



#----------------------------------------------
STOP_BUTTON_X=300
STOP_BUTTON_Y=150

Button_Forward = tk.Button(text="前進", width=4, height=2)
Button_Forward.bind("<Button-1>", Forward_Reset)
Button_Forward.place(x=STOP_BUTTON_X, y=STOP_BUTTON_Y-100)

Button_Left = tk.Button(text="左回転", width=4, height=2)
Button_Left.bind("<Button-1>", Left_Reset)
Button_Left.place(x=STOP_BUTTON_X-100, y=STOP_BUTTON_Y)

Button_Back = tk.Button(text="後退", width=4, height=2)
Button_Back.bind("<Button-1>", Back_Reset)
Button_Back.place(x=STOP_BUTTON_X, y=STOP_BUTTON_Y+100)

Button_Right = tk.Button(text="右回転", width=4, height=2)
Button_Right.bind("<Button-1>", Right_Reset)
Button_Right.place(x=STOP_BUTTON_X+100, y=STOP_BUTTON_Y)

Button_Stop = tk.Button(text="停止", width=4, height=2)
Button_Stop.bind("<Button-1>", Stop_Reset)
Button_Stop.place(x=STOP_BUTTON_X, y=STOP_BUTTON_Y)



var = tk.DoubleVar()
value = tk.Scale(root, label='速さ', length=300, tickinterval=10, orient='h', from_=0, to=100, variable=var, command=State)
value.place(x=175, y=300)

label1= tk.Label(root)
label1.place(x=350, y=400)

label2 = tk.Label(root)
label2.config(text="停止")
label2.place(x=300, y=400)
root.mainloop()