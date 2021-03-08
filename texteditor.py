import os
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
# create root window 
root = Tk()

# design 
root.geometry("300x300")
root.minsize(height = 500, width = 500)
root.title('The Archive')

global text_file
text_file = False

# Menu (File, Edit, ygolohcysp)
my_menu = Menu(root)
root.config(menu= my_menu)

# Add file menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu = file_menu)
file_menu.add_command(label='New', command = lambda:new_file())
file_menu.add_command(label='Open', command = lambda:open_file())
file_menu.add_command(label='Save', command = lambda:save_file())
file_menu.add_command(label='Save As', command = lambda:saveas_file())
file_menu.add_separator()
file_menu.add_command(label='Exit',command = root.quit)

# new window function
def new_file():
	# delete previous text in text box
	text_info.delete('1.0', END)
	# set a new title to text box
	root.title('New Archive')

	# 
	global text_file
	text_file = False

# open file function
def open_file():
	# open file/finder browser 
	file = askopenfile(initialdir = '/Documents/', filetypes = [('All Files', '*.*')], defaultextension = '.txt')

	# check to see if there is a file name
	if file:
		# make a global variable
		global text_file
		text_file = file

	# open the file
	if file is not None:
		root.title(os.path.basename(file.name)) # selected file title
		text_info.delete('1.0', END) # delete previous text  
		f = open(file.name, 'r') # read selected file 
		text_info.insert('1.0', f.read()) # insert selected file
	else:
		print('Could not open file')

# save file function
def save_file():
	global text_file
	if text_file:
		# save the file 
		text_to_save = open(text_file.name, 'w')
		text_to_save.write(text_info.get('1.0', END))
		# close the file
		text_to_save.close()
	else:
		saveas_file()


# save as file function
def saveas_file():
	# open file/finder browser
	file = asksaveasfile(initialdir = '/Documents/', filetypes = [('All Files', '*.*')], defaultextension = '.txt')
	if file is not None:
		save_info = text_info.get('1.0', END) # text to save
		file.write(save_info) # write the file to save
	else:
		pass

# Add Edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu= edit_menu)
edit_menu.add_command(label='Cut', command = lambda:cut_text(False))
edit_menu.add_command(label='Copy', command = lambda:copy_text(False))
edit_menu.add_command(label='Paste', command = lambda:paste_text(False))
edit_menu.add_command(label='Redo', command = lambda:redo_text())
edit_menu.add_command(label='Undo', command = lambda:undo_text())

# cut function
def cut_text(e):
	global selected
	if text_info.selection_get():
		# grab highlighted text
		selected = text_info.selection_get()
		# delete highlighted text 
		text_info.delete('sel.first', 'sel.last')

# copy function
def copy_text(e):
	global selected
	if text_info.selection_get():
		# grab highlighted text
		selected = text_info.selection_get()

# paste function
def paste_text(e):
	global selected
	if selected:
		position = text_info.index(INSERT)
		text_info.insert(position, selected)

# redo function
def redo_text():
	text_info.edit_redo()

# undo function
def undo_text():
	text_info.edit_undo()	


# Add Options Menu
options_menu = Menu(my_menu)
my_menu.add_cascade(label = 'Options', menu = options_menu)
options_menu.add_command(label = 'Light Mode', command = lambda:nightmode_off())
options_menu.add_command(label = 'Dark Mode', command = lambda:nightmode_on())

# night mode off 
def nightmode_off():
	main_color = 'white'
	second_color = 'white'
	text_color = 'black'

	root.config(bg = main_color)
	text_info.config(bg = second_color, fg = text_color, selectforeground = 'blue')

# nightmode on
def nightmode_on():
	main_color = 'black'
	second_color = 'black'
	text_color = 'white'

	root.config(bg = main_color)
	text_info.config(bg = main_color, fg = text_color)


# implementing scroll bar functionality
scrollbar = Scrollbar(root)

# packing the scrollbar function
scrollbar.pack(side=RIGHT, fill = Y)

# adding text 
text_info = Text(root, font = ('Typewritter', 16 ), selectforeground = 'yellow', undo=True, yscrollcommand = scrollbar.set, highlightthickness = 0)

text_info.pack(fill = BOTH)

# configuring the scrollbar
scrollbar.config(command = text_info.yview)

# widgets, buttons, etc here
root.mainloop()

