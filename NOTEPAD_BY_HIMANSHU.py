############################################################################################################################################
# Welcome to the notepad Made By - Himanshu Mahajan 
# this can do that every function that a normal notepad can do 
# every function is binded to shortcut keys 
# MADE BY ''''' HIMANSHU MAHAJAN ''''
############################################################################################################################################
from tkinter import *                                      # library for gui support 
from tkinter.filedialog import *						   # library for opening and saving file dialog 
from tkinter import messagebox,scrolledtext,colorchooser   # library for messagebox ,scrolled text , theme 
import datetime 										   # library for printing current time (here)
import webbrowser                                          # library for opening the google page for search 
import win32api                                            # library for getting the default printer of the system 
import win32print                                          # library for printing  and using the system default printer
import tempfile                                            # library for making a temporary file for printing 
############################################################################################################################################
class Notepad :                                            # creating class for notepad main window 
	def __init__ (self):                                   # defining __init__ function to have its properties for all other functions in class 
		self.__win = Tk()                                  # creating main window for program
		self.__screen_width = self.__win.winfo_screenwidth()# getting system window width for perfect geometry
		self.__screen_height = self.__win.winfo_screenheight()# getting system window height for perfect geometry
		self.__win.geometry(f"{self.__screen_width}x{self.__screen_height}")# giving the geometry to the wiindow 
		self.__win.title("  NOTEPAD - BY   \" HIMANSHU MAHAJAN \"") # giving the title to the window 
		self.__files = [('Text Document', '*.txt')]                 # getting the extension of the files for saving and opening
		self.__text_area = scrolledtext.ScrolledText(self.__win, width = self.__screen_width,height = self.__screen_height 
			,wrap = WORD,bg = "white",fg = "black", font = ('helvetica', 12),undo = True)  # creating the area for writting here used is scrolledtext
		self.__text_area.insert(INSERT," Welcome To Notepad Created By \"HIMANSHU MAHAJAN\" ") # inserting to the text area
		self.__newfilesaved = False # variables for getting the state of save 
		self.__saved = False        # same here
############################################################################################################################################
# creating Menu Bar
############################################################################################################################################
		self.__menubar = Menu(self.__win)                               # defining the main menu bar on window 
#------------------------------------------------------### File Menu ###-----------------------------------------------------------------------------
		self.__file = Menu(self.__menubar,tearoff = 0 )                 # registering a place for file menu
		self.__menubar.add_cascade(label = "File",menu  = self.__file)  # adding cascade for file 
		self.__file.add_command(label = "New File 	",command = lambda:self.__new(None,"nf"),accelerator = "Ctrl+N" ) # command for newfile option
		self.__file.add_command(label = "New Window 	",command = lambda:self.__new(None,"nw"),accelerator = "Ctrl+Shift+N" ) # command for newwindow option
		self.__file.add_command(label = "Open File... 	",command =lambda:self.__open("o"),accelerator = "Ctrl+O" ) # command for open file option
		self.__file.add_command(label = "Save 	",command = lambda:self.__save("save"),accelerator = "Ctrl+S" ) # command for save option
		self.__file.add_separator()                                                                             # adding separator
		self.__file.add_command(label = "Print 	",command =lambda: self.__print("p"),accelerator = "Ctrl+P" )   # command for print option
		self.__file.add_separator()                                                                             # adding separator
		self.__file.add_command(label = "Exit 	",command = lambda:self.__close ("cl") ,accelerator = "Alt+F4" )# command for exit
#-------------------------------------------------------### Edit Menu ###----------------------------------------------------------------------------		
		self.__edit = Menu(self.__menubar,tearoff = 0 )                                                         # registering a place for edit menu
		self.__menubar.add_cascade(label = "Edit",menu  = self.__edit)                                          # adding cascade for edit
		self.__edit.add_command(label = "Theme 	",command = lambda:self.__theme("theme"),accelerator = "Ctrl+T" )# adding commandfor theme option
		self.__edit.add_command(label = "Default Font... 	",command = lambda:self.__default("dt","dt"),accelerator = "Ctrl+Shift+T")# for default theme option
		self.__edit.add_separator()                                                                              # adding separator 
		self.__edit.add_command(label = "Undo 	",command = lambda : self.__text_area.event_generate("<<Undo>>") ,accelerator = "Ctrl+Z" )# for undo option
		self.__edit.add_command(label = "Redo	",command = lambda : self.__text_area.event_generate("<<Redo>>") ,accelerator = "Ctrl+Y" )# for redo option 
		self.__edit.add_separator()                                                                              # adding separator 
		self.__edit.add_command(label = "Cut	",command = lambda: self.__text_area.event_generate("<<Cut>>") ,accelerator = "Ctrl+X" ) # for cut option
		self.__edit.add_command(label = "Copy 	",command = lambda: self.__text_area.event_generate("<<Copy>>") ,accelerator = "Ctrl+C" )# for copy option 
		self.__edit.add_command(label = "Paste 	",command = lambda: self.__text_area.event_generate("<<Paste>>") ,accelerator = "Ctrl+V" )# for paste option
		self.__edit.add_separator()                                                                              # adding separator
		self.__edit.add_command(label="Select All...  ", command=lambda: self.__text_area.event_generate("<<SelectAll>>"),accelerator = "Ctrl+A")# for selectall option
		self.__edit.add_separator()                                                                              # adding separator 
		self.__edit.add_command(label = "Search On Google... 	",command = lambda:self.__search('search'),accelerator = "Ctrl+e")# for searching on google 
#------------------------------------------------------### Format Menu ###------------------------------------------------------------------------------------
		self.__format= Menu(self.__menubar,tearoff = 0 )                          # registering place for format menu 
		self.__menubar.add_cascade(label = "Format",menu  = self.__format)        # adding cascade for format
		self.__format.add_command(label = "Date And Time 	",command = lambda:self.__datetime("dt"),accelerator = "F5") # command for date and time
		self.__format.add_separator()                                             # adding separator 
		self.__format.add_command(label = "Font... 	",command = lambda:self.__font("f"),accelerator = "Ctrl+F") # for font 
		self.__format.add_command(label = "Default Font... 	",command = lambda:self.__default("df","df"),accelerator = "Ctrl+Shift+F") # for default font
#------------------------------------------------------### About Menu ###----------------------------------------------------------------------------------------
		self.__about = Menu(self.__menubar,tearoff = 0 )                   # registering place for about menu
		self.__menubar.add_cascade(label = "About",menu  = self.__about)   # adding cascade for about 
		self.__about.add_command(label = "About Notepad",command = lambda:self.__About("ab"),accelerator = "F1" ) # command for about notepad
		self.__about.add_separator()                                       # adding separator 
		self.__about.add_command(label = "MADE BY \"HIMANSHU MAHAJAN\"",font=('MV Boli',12,"bold"),state = DISABLED) # command for just showing name 
#------------------------------------------------------### Name Menu ###---------------------------------------------------------------------------------------
		self.__himanshu = Menu(self.__menubar,tearoff = 0 )                                                          # registering place for name on menubar
		self.__menubar.add_cascade(label = "MADE BY \"HIMANSHU MAHAJAN\"",menu  = self.__himanshu,state = DISABLED)  # adding cascade for name 
###############################################################################################################################################
# Binding all the menu options and other functions also
###############################################################################################################################################
		self.__win.bind('<Control-s>',lambda save :self.__save(save))             # Binding save option 
		self.__win.bind('<Control-n>',lambda nf :self.__new(nf,"nf"))             # Binding new fie opton 
		self.__win.bind('<Control-Shift-N>',lambda nw :self.__new(nw,"nw"))       # Binding new window option
		self.__win.bind('<Control-o>',lambda o:self.__open(o))                    # Binding open option
		self.__win.bind('<Control-p>',lambda p:self.__print(p))                   # Binding Print option
		self.__win.bind('<Control-t>',lambda t : self.__theme(t))                 # Binding theme option
		self.__win.bind('<Control-f>',lambda f : self.__font(f))                  # Binding Font option
		self.__win.bind('<Control-e>',lambda se : self.__search(se))              # Binding search on google option
		self.__win.bind('<Control-Shift-F>',lambda df : self.__default(df,'df'))  # Binding default Font option
		self.__win.bind('<Control-Shift-T>',lambda dt : self.__default(dt,'dt'))  # Binding default theme option
		self.__win.bind('<Key-F5>',lambda dt : self.__datetime(dt))               # Binding date and time option 
		self.__win.bind('<Key-F1>',lambda ab : self.__About(ab))		          # Binding about option
		self.__win.bind('<Alt-F4>',lambda cl : self.__close(cl))                  # Binding exit option
#---------------------------------------### Wraping  main window ###-------------------------------------------------------------------------------
		self.__text_area.pack(fill= BOTH , expand =True)                    # Packing text area for writing 
		self.__text_area.focus()                                            # giving focus to text area 
		self.__win.config(menu = self.__menubar)                            # configuring the menubar on main window
		self.__win.protocol("WM_DELETE_WINDOW",lambda :self.__close("cl"))  # Binding the Close button with close function
		self.__win.mainloop()                                               # Calling the main event for main window
########################################################################################################################################################
# Save functon for saving the files
########################################################################################################################################################
	def __save(self,event):                     # defining the function save with self as a class inbuilt object and event to call it with shortcut key
		try:                                    # using try and except approach to save from an unknown error
			self.__file = asksaveasfile(title = 'Save File By - "Himanshu Mahajan"',initialfile = 'untitled.txt',
				filetypes =self.__files, defaultextension = self.__files) # asking for saving file to a desired folder
			if self.__file == None:             # if user canceled the process of saving in dialog then current file is not saved
				self.__saved = False            # storing False to a variable which can be used to get the state of current file
				self.__newfilesaved = False     # simmilarly for new file opened storing False 
			else :                              # if user choosed the path to save the file 
				self.__saved = True             # storing True to the same variable which is used above 
				self.__newfilesaved = True      # simmilarly for new file opened
			# at last writing to a file and deleting the old content  of the file if already exists there 
			self.__file.name = None if self.__file.name == "" else (open(self.__file.name,"w").write(self.__text_area.get(1.0,END)).close())  
		except:                  # if any error presists then instead of getting or showing error do nothing so that further excecution dont get affected 
			None                 # doing nothing when unknown error occured
#########################################################################################################################################################
# new function for getting new file and new window 
#########################################################################################################################################################
	def __new(self ,event ,a): # defining the function new with self as a class inbuilt object event to call with shortcut key and a parameter for new file
		try:                   # using try and except approach to save from an unknown error
			if a == "nf":      # if a parameter is coming from newfile option of menubar
				self.__ask = messagebox.askyesno("  NOTEPAD - BY   \" HIMANSHU MAHAJAN \"" , "DO YOU WANT TO SAVE FILE ?") # asking to save previous opened file
				if self.__ask == True:                                        # if user want to save previous opened file 
					self.__save("save")                                       # calling the save function to save previous opened file
					self.__saved = True                                       # storing True on the variable to use it for getting file is saved or not
					self.__newfilesaved = True                                # same here also but for new file opened
				else:                                                         # if the don't want to save the previous opend file
					self.__text_area.delete("1.0",END)                        # deleting the contents of the text area
					self.__saved = True                                       # storing saved as True for prevous file 
					self.__newfilesaved = False                               # new file opened is stored as False for saving 
			else :                                                            # if the parameter is not for new file option
				self.__saved = False                                          # Means file is not saved 
			(self.__win.destroy() , self.__init__()) if a == "nw" else None   # parameter is for new window,destroying last window and calling init function
		except:                                                               # if an unknown error encountered
			None                                                              # do nothing
#########################################################################################################################################################
# open function for opening a file 
#########################################################################################################################################################
	def __open(self,event): # defining the function open with self as a class inbuilt object event to call with shortcut key
		try:                # using try and except approach to save from an unknown error
			self.__file = askopenfile(title = ' Open File By - "Himanshu Mahajan"',filetypes = self.__files , defaultextension = self.__files)# asking to open a file 
			if self.__file != "":                                       # if the user choosed a path 
				self.__content = ""                                     # a variable for adding having empty string for storing the content of the file 
				self.__opened_file = open (self.__file.name,mode='r')   # opening the file in r mode so that to retain last written content of the file 
				self.__text_area.delete("1.0",END)                      # deleting the content written on text area 
				for lines in self.__opened_file.read().split("\n"):     # reading the content of opened file using a for loop 
					self.__content = self.__content+lines+"\n"          # storing the content of the file to a variable after each loop
				self.__text_area.insert(INSERT,self.__content)          # inserting the variable stored for content of the file to the text area
				self.__saved = False                                    # storing the state of file as False 
				self.__newfilesaved = False                             # same here
		except:                                                         # if an unknown error has occured
			None                                                        # do nothing 
##########################################################################################################################################################
# print function for printing the txt file
##########################################################################################################################################################
	def __print(self,event): # defining the function print with self as a class inbuilt object event to call with shortcut key
		try:                 # using try and except approach to save from an unknown error
			file = tempfile.mktemp(".txt") # making a temporary file to write on it the contents from the text area done using tempfile library
			open(file,"w").write(self.__text_area.get("1.0",END)) # opening the temp file and writting the contents from the text area to this file
			win32api.ShellExecute(0,"print",file,'/d:"%s"' % win32print.GetDefaultPrinter(),".",0) # printing the file # search this method for more info
		except:                                                        # if an unknown error has occured
			None                                                       # do nothing
##########################################################################################################################################################
# close function for asking to save file before exiting
##########################################################################################################################################################
	def __close (self,event): # defining the function print with self as a class inbuilt object event to call with shortcut key
		if self.__saved == True and self.__newfilesaved == True: # if the files are saved already 
			self.__win.destroy()                                 # destroying the window easily as files are saved
		else:                                                    # if the files are not saved 
			self.__ask = messagebox.askyesno("  NOTEPAD - BY   \" HIMANSHU MAHAJAN \"" , "DO YOU WANT TO SAVE FILE ?") # asking the user to save file 
			if self.__ask == True:                               # if the user want to save the file
				self.__save("save")                              # calling the save function to save the file 
				self.__win.destroy()                             # after saving the file exit 
			else:	                                             # if user don't want to save the file 
				self.__win.destroy()                             # destroying the window 
#########################################################################################################################################################
# datetime function for inserting the current date and time text area
#########################################################################################################################################################
	def __datetime(self,event): # defining the function datetime with self as a class inbuilt object event to call with shortcut key
		self.__text_area.insert(INSERT,datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S")) # inserting the current date amd time in 12 hrs format
########################################################################################################################################################
# font function for changing the font in the text area
########################################################################################################################################################
	def __font(self,event):         # defining the function font with self as a class inbuilt object event to call with shortcut key
		try:                        # using try and except approach to save from an unknown error
			def font_changed(font): # defining the function font_changed to change the font 
				self.__text_area['font'] = font # changing the font 
			self.__win.call('tk', 'fontchooser', 'configure','-title','FONT CHOOSER BY - "HIMANSHU MAHAJAN" ' ,'-font', 'helvetica 12'
				, '-command', self.__win.register(font_changed)) # calling the font dialog to change the font of the text # search for more details
			self.__win.call('tk', 'fontchooser', 'show')         # this command shows the dialog of fontchooser
		except:                                                  # if an unknown error encountered
			None                                                 # do nothing
#######################################################################################################################################################
# theme function for changing the forground and background color 
#######################################################################################################################################################
	def __theme(self,event):  # defining the function font with self as a class inbuilt object event to call with shortcut key
		try:                  # using try and except approach to save from an unknown error
		# here _, is used to get only code for the color if not used then it will be a tuple and we need only second element of this tuple hence using this
		# '_' means leaving first element of the tuple and ',' means all other elements after first one 
			_, self.__color = colorchooser.askcolor(title = 'Color For Foreground   By - "Himanshu Mahajan" ') # asking the color from user for fg 
			self.__text_area ['fg'] = self.__color                                                             # setting the color for fg 
			_, self.__color = colorchooser.askcolor(title = 'Color For Background   By - "Himanshu Mahajan" ') # asking the color from user for bg 
			self.__text_area ['bg'] = self.__color                                                             # setting the color for bg 
		except:                                                                                                # if an unknown error encountered 
			None                                                                                               # do nothing
#######################################################################################################################################################
# About function for infomation of the notepad
#######################################################################################################################################################
	def __About(self,event): # defining the function About with self as a class inbuilt object event to call with shortcut key
		try:                 # using try and except approach to save from an unknown error
			self.__write = "!!! Welcome To Notepad By Himanshu Mahajan !!!\
			\n This Is Made Using Python In Sublime Text Editor \
			\n Please Rate My Application\n \
			\n!!!\"HARD WORK IS THE KEY TO SUCESS BUT SMART WORK CLEARS THE WAY TO SUCESS\" !!!\n \
			 BY - \"Himanshu Mahajan\""                                                                # variable having info about notepad as a string
			messagebox.showinfo("ABOUT NOTEPAD BY - \"Himanshu Mahajan\"",message = str(self.__write)) # showing amessage about the info 
		except:                                                                                        # if an unknown error encountered
			None                                                                                       # do nothing
########################################################################################################################################################
# default function for getting the deafult settings for theme and font
########################################################################################################################################################
	def __default(self,event,what): # defining the function About with self as a class inbuilt object event to call with shortcut key and a paramater 
		if what == "df":            # if the user want to change the default settings for font
			self.__text_area['font'] = ('helvetica', 12) # changing the font to default 
		elif what == "dt":          # if the user want to change the default settings for theme
			self.__text_area['fg'] = 'black' # setting the default foreground color 
			self.__text_area['bg'] = 'white' # setting the default background color 
########################################################################################################################################################
# search function for searching on the google 
########################################################################################################################################################
	def __search (self,event):  # defining the function search with self as a class inbuilt object event to call with shortcut key
		self.__default_browser = webbrowser.get() # getting system default webbrowser using webbrowser module
		try:                                      # using try and except approach to save from an unknown error
			self.__search_word = self.__text_area.get(SEL_FIRST, SEL_LAST) # getting the selected sentence from the text area
		except:                                   # if notting is selected in the text area 
			self.__search_word = " "              # word to search is just nothing
		self.__default_browser.open(f"https://www.google.com/search?q={self.__search_word}") # this will search the word using google 
########################################################################################################################################################
# starting the main program
########################################################################################################################################################
if __name__ == "__main__": # always __name__ is equal to '__main__' in python if no error occured
	try :                  # using try and except approach to save from an unknown error
		wind = Notepad()   # creating a object or instance of the class Notepad
	except :               # if any error has occured 
		messagebox.showerror("Error","AN ERROR HAS OCCURED") # showing the message that a error has occured 
############################################################## FINISH ##################################################################################