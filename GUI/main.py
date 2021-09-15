import os
import tkinter as tk
from tkinter import Frame, filedialog as fd
from tkinter import Button, Canvas, Entry, Label, ttk
from tkinter.constants import END
from PIL import ImageTk, Image

dirname = os.path.dirname(__file__)

class MainApp():
    def __init__(self):

        self.root = tk.Tk()
        
        self.root.title("NAB Insurance")
        self.root.geometry("800x550")

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

        self.appTab = ttk.Notebook(self.root)
        self.loadDataFrame = Frame(self.appTab, width=600, height=400)
        self.loadDateAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.timeAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.keywordAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.alcoholAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.locationAnalysisFram = Frame(self.appTab, width=600, height=400)

        self.loadDataFrame.pack(fill="both", expand=1)
        self.loadDateAnalysisFrame.pack(fill="both", expand=1)
        self.timeAnalysisFrame.pack(fill="both", expand=1)
        self.keywordAnalysisFrame.pack(fill="both", expand=1)
        self.alcoholAnalysisFrame.pack(fill="both", expand=1)
        self.locationAnalysisFram.pack(fill="both", expand=1)

        self.appTab.add(self.loadDataFrame, text="Load Data")
        self.appTab.add(self.loadDateAnalysisFrame, text="Date Analysis")
        self.appTab.add(self.timeAnalysisFrame, text="Time Analysis")
        self.appTab.add(self.keywordAnalysisFrame, text="Keyword Analysis")
        self.appTab.add(self.alcoholAnalysisFrame, text="Alcohol Analysis")
        self.appTab.add(self.locationAnalysisFram, text="Location Analysis")

        #adding widgets to screen
        self.logoCanvas.grid(row=0, column=0)
        self.selectFileBtn.grid(row=0, column=1)
        self.fileNameLabel.grid(row=0, column=2)
        self.fileName.grid(row=0, column=3, columnspan=2)
        self.loadFileBtn.grid(row=0, column=5)
        self.appTab.grid(row=3, column=0, columnspan=6)

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
