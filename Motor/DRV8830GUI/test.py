import tkinter 

root = tkinter.Tk()
val = tkinter.IntVar()
val.set(0)

def func(scl):
	label.config(text = 'Value = %d' % int(scl))
	
label = tkinter.Label(root, text = 'value = %d' % val.get())
label.pack()


s = tkinter.Scale(root, label='Scale', orient = 'h', from_= 0, to = 100, showvalue = True, variable = val, command = func)
s.pack()
root.mainloop()
