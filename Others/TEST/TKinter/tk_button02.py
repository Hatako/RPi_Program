# coding:utf-8

import Tkinter 

root=Tkinter.Tk()


def func():
	label.config(text='Pushed')


label=Tkinter.Label(root, text='Push Button')
label.pack()

button=Tkinter.Button(root, text='Push!', command=func)
button.pack()
root.mainloop()
