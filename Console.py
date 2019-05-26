# Something I made while I was bored.

from tkinter import *
import tkinter as tk

def StartMove(event):
	console.x = event.x
	console.y = event.y

def StopMove(event):
	console.x = None
	console.y = None

def OnMotion(event): 
	deltax = event.x - console.x
	deltay = event.y - console.y
	x = console.winfo_x() + deltax
	y = console.winfo_y() + deltay
	console.geometry("+%s+%s" % (x, y))
def exitProgram():
	raise SystemExit()
class Console(tk.Frame):
	def __init__(self, master = None):
		tk.Frame.__init__(self,master)
		self.page_settings()
		self.topFrame()
		self.mainFrame()
		self.commandBar()
		self.mainloop()
	def page_settings(self):
		self.master.geometry("600x400+250+250")  # W x H
		self.master.resizable(height = False, width = False)
		self.master.overrideredirect(True)
		self.master.attributes('-topmost', True)##004c80
		self.master.configure(background = 'black')
	def topFrame(self):
		topFrameDragable = tk.Frame(self.master, width = 150, background = 'black', highlightbackground = 'white', highlightthickness = 3,height = 30, relief = RIDGE, borderwidth = 0)
		topFrameDragable.pack(expand = True, fill = 'x', anchor = 'n')
		topFrameDragable.bind("<ButtonPress-1>", StartMove)
		topFrameDragable.bind("<ButtonRelease-1>", StopMove)
		topFrameDragable.bind("<B1-Motion>", OnMotion)
		titleWindow = tk.Label(topFrameDragable, text = 'Console Verison 1.0 Beta', font = ('New Times Roman', 11, 'bold'))
		titleWindow.configure(background = 'black',foreground = 'green')
		titleWindow.place(x = 0 , y = 0)
		xButton = tk.Button(topFrameDragable, text = 'X', font = ('New Times Roman', 10), borderwidth = 0, command = lambda:exitProgram())
		xButton.configure(background = 'black', foreground = 'green')
		xButton.place(x = 580, y = 0)
	def mainFrame(self):
		global mainWindow
		mainWindow = tk.Text(width = 73, background = 'black',foreground = 'white', highlightbackground = 'white', highlightthickness = 3, height = 16)
		mainWindow.configure(font=('New Times Roman', 11, 'bold'))
		mainWindow.place(x = 0, y = 40)
	def commandBar(self):
		global cmdBar
		cmdBar = tk.Text(background = 'black', foreground = 'white', width = 73, height = 2, highlightbackground = 'green', highlightthickness = 3)
		cmdBar.configure(font=('New Times Roman', 11, 'bold'))
		cmdBar.place(x = 0, y = 350)
		cmdBar.bind("<Button-1>", checkOnFocus)
		cmdBar.bind("<FocusOut>", removeCheckOnFocus)
		cmdBar.bind("<Return>", executeCommand)


class consoleMessages(object):
	def __init__(self, message = None, color = None):
		if color is None:
			mainWindow.insert(END, message + "\n")
		else:
			mainWindow.tag_configure(str(color), foreground = str(color))
			mainWindow.insert(END, message + "\n", str(color))
		console.update()
		console.update_idletasks()
		cmdBar.delete('1.0', END)
		cmdBar.update()

def checkOnFocus(event):
	global FocusedOn
	FocusedOn = True
def removeCheckOnFocus(event):
	global FocusedOn
	FocusedOn = False
def executeCommand(event):
	if FocusedOn: 
		if '\n' in cmdBar.get('1.0','end-1c'):
			cmdBar.get('1.0','end-1c').strip('\n') # idk sometimes it leaves \n in entry dont know why if ur reading this then plz tell me
			# why it leaves \n in text box after its finished...
			# could probably improve it since it still has bugs but its 2:05 AM im tired.
		if 'print' in cmdBar.get('1.0','end-1c').split(' ')[0]:
			if '..color' in cmdBar.get('1.0','end-1c').split(' '):
				colorPosition = []
				for i,v in enumerate(cmdBar.get('1.0','end-1c').split(' ')):
					if v == '..color':
						colorPosition.append(i)
						break
			else:
				consoleMessages(cmdBar.get("1.0","end-1c").strip("print"))
				return
			colorNum = colorPosition[0] + 1
			colorChoice = (cmdBar.get('1.0','end-1c').split(' ')[colorNum])
			toPrint = (cmdBar.get('1.0','end-1c').strip("print ").strip('..color %s'%(colorChoice)))
			consoleMessages(toPrint,colorChoice)
			return
	else:
		print (FocusedOn)
console = tk.Tk()
Console(master = console)
