#!/usr/bin/env python3

"""
ZetCode Tkinter Tutorial

In this script, we use the pack manager
to position two buttons in the
bottom-right corner of the window.

Author: Jan Bodnar
Last modified by author: April 2019
Website: www.zetcode.com

Modified by: Jessica Angela Campisi
Modified date: August 2019
"""

from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.master.title("Buttons")  # title of app as it appears
        self.style = Style() # appearance of app style
        self.style.theme_use("default") # theme is set to default. alt or classic are options.

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        self.pack(fill=BOTH, expand=True)

        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)


def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()