from tkinter import *

def changeText():
    #function to change the label
	#to what appears on the Entry field
	#when the button is pressed
	global myLabel
	myLabel.config(myLabel,text=myVar.get())

	
root = Tk()

myVar = StringVar()  #creating instance of String var to get the entry
myEntry = Entry(root, textvariable = myVar) #creating the entry field 
#creating a label to print the what on the entry when a button is pressed
myLabel = Label(root,text=myEntry) 
myButton = Button(root, text="change", command=changeText) #Creating the button

#packing our item on the screen
myEntry.pack()
myButton.pack()
myLabel.pack()

root.mainloop()