"""
8/7 今までのプログラムを全て結合し実験用のGUI作成する
8/8 持ち上げボタン, 受け渡しボタンを作成
"""


import RPi.GPIO as GPIO		
import time
import tkinter as tk
from Adafruit_PCA9685 import PCA9685

root = tk.Tk()
root.title("移動ロボットを動かそう!")
root.geometry("1920x1080")

# HAT MDD10の設定
GPIO.setmode(GPIO.BCM)			
GPIO.setwarnings(False)			# enable warning from GPIO
AN1 = 12				# set pwm1 pin on MD10-hat
AN2 = 13				# set pwm2 pin on MD10-Hat
DIG1 = 26				# set dir1 pin on MD10-Hat(右)
DIG2 = 24				# set dir2 pin on MD10-Hat(左)
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
right_wheel = GPIO.PWM(AN1, 100)		# set pwm for M1
left_wheel = GPIO.PWM(AN2, 100)			# set pwm for M2
SPEED_RIGHT = 0
SPEED_LEFT = 0
right_wheel.start(SPEED_RIGHT)
left_wheel.start(SPEED_LEFT)


# Servo/PWM Pi HATの設定
pwm = PCA9685(0x40)
pwm.set_pwm_freq(50)
pwm.set_pwm(0, 0, 395)
pwm.set_pwm(1, 0, 340)
pwm.set_pwm(2, 0, 240)
pwm.set_pwm(4, 0, 200)


def forward(event):
    global SPEED_RIGHT, SPEED_LEFT
    if (SPEED_RIGHT + 10 or SPEED_LEFT + 10) > 50:
        label1.config(text="左: {0}  右: {1}  操作不可".format(SPEED_LEFT, SPEED_RIGHT))
    else:
        SPEED_RIGHT = SPEED_RIGHT + 10
        SPEED_LEFT = SPEED_LEFT + 10
        if SPEED_RIGHT >= 0:
            GPIO.output(DIG1, GPIO.HIGH)
        else:
            GPIO.output(DIG1, GPIO.LOW)
        if SPEED_LEFT >= 0:
            GPIO.output(DIG2, GPIO.HIGH)
        else:
            GPIO.output(DIG2, GPIO.LOW)
        right_wheel.start(abs(SPEED_RIGHT))
        left_wheel.start(abs(SPEED_LEFT))
        label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))

def back(event):
    global SPEED_RIGHT, SPEED_LEFT
    if (SPEED_RIGHT - 10 or SPEED_LEFT - 10) < -50:
        label1.config(text="左: {0}  右: {1}  操作不可".format(SPEED_LEFT, SPEED_RIGHT))
    else:
        SPEED_RIGHT = SPEED_RIGHT - 10
        SPEED_LEFT = SPEED_LEFT - 10
        if SPEED_RIGHT >= 0:
            GPIO.output(DIG1, GPIO.HIGH)
        else:
            GPIO.output(DIG1, GPIO.LOW)
        if SPEED_LEFT >= 0:
            GPIO.output(DIG2, GPIO.HIGH)
        else:
            GPIO.output(DIG2, GPIO.LOW)
        right_wheel.start(abs(SPEED_RIGHT))
        left_wheel.start(abs(SPEED_LEFT))
        label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))

def left(event):
    global SPEED_RIGHT, SPEED_LEFT
    if (SPEED_RIGHT + 5 > 50) or (SPEED_LEFT - 5 < -50) :
        label1.config(text="左: {0}  右: {1}  操作不可".format(SPEED_LEFT, SPEED_RIGHT))
    else:
        SPEED_RIGHT = SPEED_RIGHT + 5
        SPEED_LEFT = SPEED_LEFT - 5
        if SPEED_RIGHT >= 0:
            GPIO.output(DIG1, GPIO.HIGH)
        else:
            GPIO.output(DIG1, GPIO.LOW)
        if SPEED_LEFT >= 0:
            GPIO.output(DIG2, GPIO.HIGH)
        else:
            GPIO.output(DIG2, GPIO.LOW)
        right_wheel.start(abs(SPEED_RIGHT))
        left_wheel.start(abs(SPEED_LEFT))
        label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))

def right(event):
    global SPEED_RIGHT, SPEED_LEFT
    if (SPEED_RIGHT - 5 < -50) or (SPEED_LEFT + 5 > 50) :
        label1.config(text="左: {0}  右: {1}  操作不可".format(SPEED_LEFT, SPEED_RIGHT))
    else:
        SPEED_RIGHT = SPEED_RIGHT - 5
        SPEED_LEFT = SPEED_LEFT + 5
        if SPEED_RIGHT >= 0:
            GPIO.output(DIG1, GPIO.HIGH)
        else:
            GPIO.output(DIG1, GPIO.LOW)
        if SPEED_LEFT >= 0:
            GPIO.output(DIG2, GPIO.HIGH)
        else:
            GPIO.output(DIG2, GPIO.LOW)
        right_wheel.start(abs(SPEED_RIGHT))
        left_wheel.start(abs(SPEED_LEFT))
        label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))


def stop(event):
    global SPEED_RIGHT, SPEED_LEFT
    SPEED_RIGHT = 0
    SPEED_LEFT = 0
    right_wheel.start(SPEED_RIGHT)
    left_wheel.start(SPEED_LEFT)
    label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))

# 持ち上げボタンが押されたときの動作
# 初期
# 0ch:395, 1ch:340, 2ch:240, 4ch:200
# getの目標値
# 0ch:448, 1ch:340, 2ch:383, 4ch:200

def get(event):
    for i in range(448-395+1):
        pwm.set_pwm(0, 0, i+395)
        time.sleep(0.005)
    for i in range(383-240+1):
        pwm.set_pwm(2, 0, i+240)
        time.sleep(0.005)
    for i in range(400-200+1):
        pwm.set_pwm(4, 0, i+200)
        time.sleep(0.005)
# 持ち上げたので0, 2chはもとに戻す
    for i in range(448-395+1):
        pwm.set_pwm(0, 0, 448-i)
        time.sleep(0.005)
    for i in range(383-240+1):
        pwm.set_pwm(2, 0, 383-i)
        time.sleep(0.005)


def pass_object(event):
    for i in range(400-200+1):
        pwm.set_pwm(4, 0, 400-i)
        time.sleep(0.005)



#----------------------------------------------
STOP_BUTTON_X=1300
STOP_BUTTON_Y=350
FONT_SIZE = 120

Button_Forward = tk.Button(text="↑", font=("", FONT_SIZE))
Button_Forward.bind("<Button-1>", forward)
Button_Forward.place(x=STOP_BUTTON_X, y=STOP_BUTTON_Y-250)

Button_Back = tk.Button(text="↓", font=("", FONT_SIZE))
Button_Back.bind("<Button-1>", back)
Button_Back.place(x=STOP_BUTTON_X, y=STOP_BUTTON_Y+250)

Button_Right = tk.Button(text="→", font=("", FONT_SIZE))
Button_Right.bind("<Button-1>", right)
Button_Right.place(x=STOP_BUTTON_X+250, y=STOP_BUTTON_Y)

Button_Left = tk.Button(text="←", font=("", FONT_SIZE))
Button_Left.bind("<Button-1>", left)
Button_Left.place(x=STOP_BUTTON_X-250, y=STOP_BUTTON_Y)

Button_Stop = tk.Button(text="○", font=("", FONT_SIZE))
Button_Stop.bind("<Button-1>", stop)
Button_Stop.place(x=STOP_BUTTON_X, y=STOP_BUTTON_Y)

Button_Get = tk.Button(text="拾う", font=("", 60))
Button_Get.bind("<Button-1>", get)
Button_Get.place(x=600, y=600)

Button_Pass = tk.Button(text="受け取る", font=("", 60))
Button_Pass.bind("<Button-1>", pass_object)
Button_Pass.place(x=600, y=800)


#var = tk.DoubleVar()
#value = tk.Scale(root, label='速さ', length=300, tickinterval=10, orient='h', from_=0, to=100, variable=var, command=State)
#value.place(x=175, y=300)

label1= tk.Label(root)
label1.config(text="停止", font=("", 40))
label1.place(x=1250, y=900)

root.mainloop()