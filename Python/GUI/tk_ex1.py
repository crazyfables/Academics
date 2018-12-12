#!/usr/bin/python3
# hello_tkinter.py by Barron Stone
# modified by Jessica Angela Campisi
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk() # Creates the window
label = ttk.Label(root, text = "Howdy, Tkinter!") # Creates a label
label.pack() # throws the label on top of the window

# place the image in the label
logo = PhotoImage(file = "python_logo.gif") # creates an image object
label.config(image = logo) # added the image to the label
label.config(compound = 'text')
label.config(compound = 'center')
label.config(wraplength = 150)

# sets the label colors and modifies placement
label.config(justify = CENTER)
label.config(foreground = 'blue', background = 'yellow')
label.config(font = {'Courier', 18, 'bold'})
label.config(compound = 'left')

# mainloop() add
root.mainloop() # runs the window outside the idle