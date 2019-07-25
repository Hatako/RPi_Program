#coding: utf-8

import Tkinter
root=Tkinter.Tk()

def func():
	print 'Pushed!'

button=Tkinter.Button(root, text='Push!', command=func)


button.pack()
root.mainloop()
