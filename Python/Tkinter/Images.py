from tkinter import *
from PIL import ImageTk, Image

root = Tk()
catPhoto = ImageTk.PhotoImage(Image.open("cat.jpg"))
myLabel = Label(root, image=catPhoto)

myLabel.pack()

root.mainloop()
