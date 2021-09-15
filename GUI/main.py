import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import Button, Canvas, Entry, Label, PhotoImage, StringVar
from tkinter.constants import END
from PIL import ImageTk, Image

dirname = os.path.dirname(__file__)

class MainApp():
    def __init__(self):

        self.root = tk.Tk()
        
        self.root.title("NAB Insurance")
        self.root.geometry("600x400")

        #canvas for logo
        self.logoCanvas = Canvas(self.root, width=100, height=50)
        self.logo = Image.open(dirname+"/images/logo.png").resize((100, 50), Image.ANTIALIAS)
        #resized logo
        self.resizedLogo= ImageTk.PhotoImage(self.logo)
        self.logoCanvas.create_image(50,20, image=self.resizedLogo)

        self.fileNameLabel = Label(self.root, text="File Name:")
        self.fileName = Entry(self.root)
        self.fileName.config(state="readonly")

        self.selectFileBtn = Button(self.root, text="SELECT FILE", command=self.selectFile)
        self.loadFileBtn = Button(self.root, text="Load", width=5, height=3)

        #adding widgets to screen
        self.logoCanvas.grid(row=0, column=0)
        self.selectFileBtn.grid(row=0, column=1)
        self.fileNameLabel.grid(row=0, column=2)
        self.fileName.grid(row=0, column=3)
        self.loadFileBtn.grid(row=0, column=4)

        self.root.mainloop()

    def selectFile(self):
        self.fileName.config(state="normal")
        self.fileName.delete(0, END)
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        
        print(filename)
        self.fileName.insert(0, filename)
        self.fileName.config(state="readonly")

app = MainApp()
