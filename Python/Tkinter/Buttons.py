from tkinter import *

def change_bg():
	global label
	Label.config(label,bg='yellow')

root = Tk()
label = Label(root, text="Embedex", bg='red')
myButton = Button(root, text="change", command=change_bg, height=5, width= 5, bg='blue', fg='white')


label.pack()
myButton.pack()

root.mainloop()

