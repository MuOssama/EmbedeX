from tkinter import *
from PIL import ImageTk, Image

def changePhoto():
		global index
		index = index+1
		if index >2:
			index = 0
		myLabel.config(myLabel, image=cats[index])

		
root = Tk()
catPhoto = ImageTk.PhotoImage(Image.open("cat.jpg"))
catPhoto2 = ImageTk.PhotoImage(Image.open("cat2.jpg"))
catPhoto3 = ImageTk.PhotoImage(Image.open("cat3.jpg"))
cats = [catPhoto,catPhoto2,catPhoto3]
index=0

myLabel = Label(root, image=catPhoto)
mybutton = Button(root, text="change photo", command=changePhoto)

mybutton.pack()
myLabel.pack()

root.mainloop()