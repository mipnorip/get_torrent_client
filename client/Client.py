from email import message
import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

from .Application import Application


class Client(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.api = Application()
        self.data = {}

        self.title("nnmclub.to parser")
        width = 582
        height = 177
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_36 = tk.Label(self)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_36["font"] = ft
        GLabel_36["fg"] = "#333333"
        GLabel_36["justify"] = "center"
        GLabel_36["text"] = "nnmclub.to parser"
        GLabel_36.place(x=190, y=10, width=191, height=30)

        self.GLineEdit_835 = tk.Entry(self)
        self.GLineEdit_835["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_835["font"] = ft
        self.GLineEdit_835["fg"] = "#333333"
        self.GLineEdit_835["justify"] = "center"
        self.GLineEdit_835["text"] = "Entry"
        self.GLineEdit_835.place(x=30, y=50, width=365, height=30)

        GButton_585 = tk.Button(self)
        GButton_585["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Поиск"
        GButton_585.place(x=460, y=50, width=101, height=30)
        GButton_585["command"] = self.GButton_585_command

        self.GListBox_315 = tk.Listbox(self)
        self.GListBox_315["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GListBox_315["font"] = ft
        self.GListBox_315["fg"] = "#333333"
        self.GListBox_315["justify"] = "left"
        self.GListBox_315.place(x=30, y=110, width=362, height=62)

        GButton_280 = tk.Button(self)
        GButton_280["bg"] = "#c0c0c0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_280["font"] = ft
        GButton_280["fg"] = "#000000"
        GButton_280["justify"] = "center"
        GButton_280["text"] = "Скачать"
        GButton_280.place(x=460, y=110, width=99, height=30)
        GButton_280["command"] = self.GButton_280_command

    def GButton_585_command(self):
        self.data = self.api.get_list(self.GLineEdit_835.get())
        [self.GListBox_315.insert(END, line.strip())
         for line in self.data.keys()]

    def GButton_280_command(self):
        self.api.get_item(self.data[self.GListBox_315.selection_get()])

    def exit(self):
        self.quit()
        self.api.quit()
