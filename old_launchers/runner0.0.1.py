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
	if txt.get() == "":
		a = "0.0.4"
		lbl.configure(text="Game End!")
		os.system("pip install ursina")
		os.system("python versions/"+a+"/YaMinecraft.py")
	elif txt.get() in version_list:
		a = combo.get()
		lbl.configure(text="Game End!")
		os.system("pip install ursina")
		os.system("python versions/"+a+"/YaMinecraft.py")
	else:
		lbl.configure(text="Wrong Version name!")

window = Tk()
window.title("YaMinecraft Launcher")

lbl = Label(window, text="Welcome to YaMinecraft Launcher!")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

btn = Button(window, text="Start game",command=clicked)
btn.grid(column=2, row=0)

window.mainloop()