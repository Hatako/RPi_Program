#coding: utf-8

import Tkinter
root=Tkinter.Tk()

def func():
	label.config(text='Pushed')


def func_event(ev):
	label.config(text='Push botton')

label=Tkinter.Label(root, text='Push Button')

label.pack()
button=Tkinter.Button(root, text='Push!', command=func)

button.pack()
button.bind('<Leave>', func_event)

root.mainloop()
