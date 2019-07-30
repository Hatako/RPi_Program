# 7/30 tkinter test

import tkinter as tk
from tkinter import messagebox

root =tk.Tk()
root.title("移動ロボットを動かそう！")
root.geometry("500x1000")

def check(event):
    text = ""
    count = 0
    if Val1.get() == True:
        text+="項目1はチェックされとるで\n"
    else:
        text+="項目1はチェックされとらんで\n"

    if Val2.get() == True:
        text+="項目2はチェックされとるで\n"
    else:
        text+="項目2はチェックされとらんで\n"
    messagebox.showinfo("確認した結果", text)


#Button = tk.Button(text="チェックを確認したろか？", width=20)
#Button.bind("<Button-1>", check)
#Button.place(x=100, y=200)

Val1 = tk.BooleanVar()
Val2 = tk.BooleanVar()

Val1.set(False)
Val2.set(False)

CheckButton1 = tk.Checkbutton(text="項目1", variable=Val1)
CheckButton1.place(x=100, y=300)

CheckButton2 = tk.Checkbutton(text="項目2", variable=Val2)
CheckButton2.place(x=100, y=350)


def sel():
    selection = "Value = {}".format(var.get())
    label.config(text=selection)
    print(var.get())

# scroll var
var = tk.DoubleVar()
scale = tk.Scale(root, variable=var)
scale.place(x=100, y=700)

button = tk.Button(root, text="Get Scale Value", command=sel)
button.place(x=100, y=800)

label = tk.Label(root)
label.place(x=100, y=900)





root.mainloop()