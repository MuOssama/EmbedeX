from tkinter import *

root = Tk() #this is main window of our GUI

textLabel1 = Label(root, text="Embedex", bg='white') #Creating the object
textLabel2 = Label(root, text="Embedex", bg='green') #Creating the object
textLabel3 = Label(root, text="Embedex", bg='blue') #Creating the object
textLabel4 = Label(root, text="Embedex", bg='red') #Creating the object

textLabel1.pack(side='left') #putting the text label (object) on the screen
textLabel2.pack(side='right') #putting the text label (object) on the screen
textLabel3.pack(side='bottom') #putting the text label (object) on the screen
textLabel4.pack(side='top') #putting the text label (object) on the screen

root.mainloop() #this updates the app





