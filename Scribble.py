import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Scribble:
	__root=Tk()

	__thisWidth=300
	__thisHeight=300
	__thisTextArea=Text(__root)
	__thisMenuBar=Menu(__root)
	__thisFileMenu=Menu(__thisMenuBar,tearoff=0)
	__thisEditMenu=Menu(__thisMenuBar,tearoff=0)
	__thisHelpMenu=Menu(__thisMenuBar,tearoff=0)
	__thisScrollBar=Scrollbar(__thisTextArea)
	__file=None

	def __init__(self,**kwargs):
		try:
			self.__root.wm_iconbitmap('F:\Python Programs\download.ico')#Abolute path for the sake of PyInstaller
			#pi=PhotoImage(file='download.png')
			#self.__root.iconphoto(False,pi)
		except:
			pass
		try:
			self.__thisWidth=kwargs['width']
			self.__thisHeight=kwargs['height']
		except KeyError:
			pass
		self.__root.title("Untitled - Scribble")

		#To center the Scribble window onto the screen
		screenWidth=self.__root.winfo_screenwidth()
		screenHeight=self.__root.winfo_screenheight()
		left=(screenWidth/2)-(self.__thisWidth/2)
		top=(screenHeight/2)-(self.__thisHeight/2)
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,self.__thisHeight,left,top))  

		#To make Auto Resizable TextArea
		self.__root.grid_rowconfigure(0,weight=1)
		self.__root.grid_columnconfigure(0,weight=1)

		self.__thisTextArea.grid(sticky=N+E+S+W)
		self.__thisFileMenu.add_command(label="New",command=self.__newFile,accelerator="Ctrl+N")
		self.__thisFileMenu.add_command(label="Open",command=self.__openFile,accelerator="Ctrl+O")
		self.__thisFileMenu.add_command(label="Save",command=self.__saveFile,accelerator="Ctrl+S")
		self.__thisFileMenu.add_separator()
		self.__thisFileMenu.add_command(label="Exit",command=self.__exitApp,accelerator="Ctrl+Q")
		self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)

		self.__thisEditMenu.add_command(label="Cut",command=self.__cut,accelerator="Ctrl+X")
		self.__thisEditMenu.add_command(label="Copy",command=self.__copy,accelerator="Ctrl+C")
		self.__thisEditMenu.add_command(label="Paste",command=self.__paste,accelerator="Ctrl+V")
		self.__thisMenuBar.add_cascade(label="Edit",menu=self.__thisEditMenu)

		self.__thisHelpMenu.add_command(label="About",command=self.__showAbout,accelerator="Ctrl+H")
		self.__thisMenuBar.add_cascade(label="Help",menu=self.__thisHelpMenu)

		self.__root.config(menu=self.__thisMenuBar)
		self.__thisScrollBar.pack(side=RIGHT,fill=Y)

		#Resize scrollbar with text in the textArea
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

		self.__root.bind('<Control-n>',self.__newFile)
		self.__root.bind('<Control-o>',self.__openFile)
		self.__root.bind('<Control-s>',self.__saveFile)
		self.__root.bind('<Control-q>', self.__exitApp)
		self.__root.bind('<Control-x>',self.__cut)
		self.__root.bind('<Control-c>',self.__copy)
		self.__root.bind('<Control-v>',self.__paste)
		self.__root.bind('<Control-h>',self.__showAbout)

	def __newFile(self,event=None):
		self.__root.title("Untitled - Scribble")
		self.__file=None
		self.__thisTextArea.delete(1.0,END)

	def __openFile(self,event=None):
		self.__file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
		if self.__file=="":
			self.__file=None
		else:
			self.__root.title(os.path.basename(self.__file)+" - Scribble")
			self.__thisTextArea.delete(1.0,END)
			file=open(self.__file,"r")
			self.__thisTextArea.insert(1.0,file.read())
			file.close()

	def __saveFile(self,event=None):
		if self.__file==None:
			self.__file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
			if self.__file == "":
				self.__file=None
			else:
				file=open(self.__file,"w")
				file.write(self.__thisTextArea.get(1.0,END))
				file.close()
				self.__root.title(os.path.basename(self.__file)+" - Scribble")
		else:
			file=open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()

	def __exitApp(self,event=None):
		self.__root.destroy()

	def __cut(self,event=None):
		self.__thisTextArea.event_generate("<<Cut>>")
	def __copy(self,event=None):
		self.__thisTextArea.event_generate("<<Copy>>")
	def __paste(self,event=None):
		self.__thisTextArea.event_generate("<<Paste>>")
	def __showAbout(self,event=None):
		showinfo("Scribble","Application for your quick scribble and notes.\nUsing Python Tkinter and OS for OS related functions.\n\nPreethi Ann Jacob\n3rd September, 2020\n\nHave a nice day :D")

	def run(self):
		self.__root.mainloop()

Scribble=Scribble(width=600,height=400)
Scribble.run()
