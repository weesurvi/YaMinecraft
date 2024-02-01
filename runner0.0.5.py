import os,sys
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox

if float(sys.version[0:3]) != 3.8:
	tkinter.messagebox.showwarning(title='Python Version Warning',message='Sorry,your Python version is too high or too low.Please use Python 3.8')
	
def getfiles():
	filenames=os.listdir("versions/")
	return filenames

version_list = getfiles()
def dlb():
	os.system("pip install ursina")
def clicked():
	a="a"
	if combo.get() == "":
		a = "0.0.4"
		lbl.configure(text="Game End!")
		os.system("python versions/"+a+"/YaMinecraft.pyc")
	elif combo.get() in version_list:
		a = combo.get()
		tkinter.messagebox.showinfo(title="Information",message="Game Start!")
		os.system("python versions/"+a+"/YaMinecraft.pyc")
	else:
		tkinter.messagebox.showwarning(title="Error",message="Wrong Version name!")

def gmd():
	a = combo.get()
	os.system("start versions/"+a+"/README.md")

window = Tk()
window.title("YaMinecraft Launcher")

lbl = Label(window, text="Welcome to YaMinecraft Launcher!")
lbl.grid(column=1, row=0)

combo = Combobox(window)
combo['values'] = version_list
combo.current(0)
combo.grid(column=0, row=1)

btn = Button(window, text="Start a specified version of the game",command=clicked)
btn.grid(column=1, row=1)

btn = Button(window, text="Get README.md",command=gmd)
btn.grid(column=2, row=1)

btn = Button(window, text="Download librarys",command=dlb)
btn.grid(column=3, row=1)

window.mainloop()