import os
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
	
def getfiles():
	filenames=os.listdir("versions/")
	return filenames

version_list = getfiles()
def clicked():
	a="a"
	if combo.get() == "":
		a = "0.0.4"
		lbl.configure(text="Game End!")
		os.system("pip install ursina")
		os.system("python versions/"+a+"/YaMinecraft.py")
	elif combo.get() in version_list:
		a = combo.get()
		lbl.configure(text="Game End!")
		os.system("pip install ursina")
		os.system("python versions/"+a+"/YaMinecraft.py")
	else:
		lbl.configure(text="Wrong Version name!")

def gmd():
	a = combo.get()
	os.system("start versions/"+a+"/README.md")

window = Tk()
window.title("YaMinecraft Launcher")

lbl = Label(window, text="Welcome to YaMinecraft Launcher!")
lbl.grid(column=0, row=0)

combo = Combobox(window)
combo['values'] = version_list
combo.current(0)
combo.grid(column=1, row=0)

btn = Button(window, text="Start a specified version of the game",command=clicked)
btn.grid(column=2, row=0)

btn = Button(window, text="Get README.md",command=gmd)
btn.grid(column=3, row=0)

window.mainloop()