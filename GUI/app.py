import os
import tkinter as tk
from tkinter import Button, Canvas, Entry, Label, Scrollbar, ttk, Frame, filedialog
from tkcalendar import DateEntry
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter.constants import BOTH, BOTTOM, END, FALSE, HORIZONTAL, LEFT, NE, NSEW, RIGHT, VERTICAL, X, Y
from PIL import ImageTk, Image
from functions import fetchData

dirname = os.path.dirname(__file__)

class MainApp():
    def __init__(self):

        self.root = tk.Tk()
        
        self.root.title("NAB Insurance")
        #frame for main menu
        self.mainFrame = Frame(self.root, padx=5, pady=5)
        self.mainFrame.place(x=75, y=75)

        self.logoFrame = Frame(self.root, padx=5, pady=5)

        #canvas for logo
        self.logoCanvas = Canvas(self.logoFrame, width=100, height=50)
        self.logo = Image.open(dirname+"/images/logo.png").resize((100, 50), Image.ANTIALIAS)
        #resized logo
        self.resizedLogo= ImageTk.PhotoImage(self.logo)
        self.logoCanvas.create_image(50,20, image=self.resizedLogo)
        self.logoCanvas.grid(row=0, column=0)
        self.logoFrame.place(x=10, y=10)

        #initialize widgets for main menu
        #widgets for load data tab
        self.fileNameLabel = Label(self.mainFrame, text="File Name:", width=40)
        self.fileNameLabel.place(x=30, y=10)
        self.fileName = Entry(self.mainFrame, width=40)
        self.fileName.place(x=30, y=10)
        self.fileName.config(state="readonly")

        self.selectFileBtn = Button(self.mainFrame, text="SELECT FILE", width=40)
        self.selectFileBtn.place(x=30, y=10)
        self.loadFileBtn = Button(self.mainFrame, text="Load", width=10, height=3)
        self.loadFileBtn.place(x=30, y=10)


        self.root.mainloop()


app = MainApp()