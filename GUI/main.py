import os
import tkinter as tk
from tkinter import Button, Canvas, Entry, Label, ttk, Frame, filedialog
from tkcalendar import DateEntry
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter.constants import END, NSEW
from PIL import ImageTk, Image

dirname = os.path.dirname(__file__)

class MainApp():

    def __init__(self):

        self.root = tk.Tk()
        
        self.root.title("NAB Insurance")
        #frame for main menu
        self.mainFrame = Frame(self.root, padx=5, pady=5)

        self.logoFrame = Frame(self.root, padx=5, pady=5)

        #canvas for logo
        self.logoCanvas = Canvas(self.logoFrame, width=100, height=50)
        self.logo = Image.open(dirname+"/images/logo.png").resize((100, 50), Image.ANTIALIAS)
        #resized logo
        self.resizedLogo= ImageTk.PhotoImage(self.logo)
        self.logoCanvas.create_image(50,20, image=self.resizedLogo)
        self.logoCanvas.grid(row=0, column=0)
        self.logoFrame.grid(row=0, column=0)

        #initialize widgets for main menu
        #widgets for load data tab
        self.fileNameLabel = Label(self.mainFrame, text="File Name:")
        self.fileName = Entry(self.mainFrame, width=40)
        self.fileName.config(state="readonly")

        self.selectFileBtn = Button(self.mainFrame, text="SELECT FILE", command=self.selectFile, width=10)
        self.loadFileBtn = Button(self.mainFrame, text="Load", width=10, height=3)

        #widgets for Date and Time Analysis
        self.startDateLabel = Label(self.mainFrame, text="Start Date:*")
        self.startDate = DateEntry(self.mainFrame, selectmode="day")
        self.endDateLabel = Label(self.mainFrame, text="End Date:*")
        self.endDate = DateEntry(self.mainFrame, selectmode="day")

        #additional widgets for Keyword Analysis
        self.keywordLabel = Label(self.mainFrame, text="Keyword:")
        self.keyword = Entry(self.mainFrame)

        #additional widgets for Alcohol Analysis
        self.startDate2Label = Label(self.mainFrame, text="Start Date:")
        self.startDate2 = DateEntry(self.mainFrame, selectmode="day")
        self.endDate2Label = Label(self.mainFrame, text="End Date:")
        self.endDate2 = DateEntry(self.mainFrame, selectmode="day")

        #additional widgets for Location Analysis
        self.locationLabel = Label(self.mainFrame, text="Location:")
        self.location = AutocompleteCombobox(self.mainFrame, completevalues=[])

        #call loadDataTab as it is our homescreen
        self.loadDataTab()

        #frame for loaded data
        self.loadedFrame = Frame(self.root, padx=5, pady=5)
        #widget for display below
        self.appTab = ttk.Notebook(self.loadedFrame)
        self.loadDataFrame = Frame(self.appTab)
        self.loadDateAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.timeAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.keywordAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.alcoholAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.locationAnalysisFram = Frame(self.appTab, width=600, height=400)

        self.appTab.bind("<<NotebookTabChanged>>", self.changeTab)

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
        self.appTab.grid(row=0, column=0, columnspan=6)
        self.loadedFrame.grid(row=1, column=0, columnspan=2)

        col_count, row_count = self.mainFrame.grid_size()

        for col in range(col_count):
            self.mainFrame.grid_columnconfigure(col, weight=100)

        for row in range(row_count):
            self.mainFrame.grid_rowconfigure(row, weight=50)

        self.root.mainloop()

    def selectFile(self):
        self.fileName.config(state="normal")
        self.fileName.delete(0, END)
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        
        print(filename)
        self.fileName.insert(0, filename)
        self.fileName.config(state="readonly")

    def changeTab(self, event):
        selectedTab = event.widget.select()
        tabText = event.widget.tab(selectedTab, "text")

        if tabText == "Load Data":
            self.loadDataTab()
        elif tabText == "Date Analysis":
            self.dateAndTimeAnalysisTab()
        elif tabText == "Time Analysis":
            self.dateAndTimeAnalysisTab()
        elif tabText == "Keyword Analysis":
            self.keywordAnalysisTab()
        elif tabText == "Alcohol Analysis":
            self.alcoholAnalysisTab()
        elif tabText == "Location Analysis":
            self.locationAnalysisTab()

    def loadDataTab(self):
        self.mainFrame.grid_forget()
        self.gridForget()
        
        self.selectFileBtn.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        self.fileNameLabel.grid(row=0, column=2)
        self.fileName.grid(row=0, column=3, columnspan=2)
        self.loadFileBtn.grid(row=0, column=5, rowspan=2)
        self.mainFrame.grid(row=0, column=1)

    def dateAndTimeAnalysisTab(self):
        self.mainFrame.grid_forget()
        self.gridForget()

        self.startDateLabel.grid(row=0, column=1)
        self.startDate.grid(row=0, column=2)
        self.endDateLabel.grid(row=0, column=3)
        self.endDate.grid(row=0, column=4)
        self.loadFileBtn.grid(row=0, column=5, rowspan=2)
        self.mainFrame.grid(row=0, column=1)

    def keywordAnalysisTab(self):
        self.mainFrame.grid_forget()
        self.gridForget()

        self.startDateLabel.grid(row=0, column=1)
        self.startDate.grid(row=0, column=2)
        self.endDateLabel.grid(row=0, column=3)
        self.endDate.grid(row=0, column=4)
        self.keywordLabel.grid(row=1, column=3)
        self.keyword.grid(row=1, column=4)
        self.loadFileBtn.grid(row=0, column=5, rowspan=2)
        self.mainFrame.grid(row=0, column=1)

    def alcoholAnalysisTab(self):
        self.mainFrame.grid_forget()
        self.gridForget()

        self.startDateLabel.grid(row=0, column=1)
        self.startDate.grid(row=0, column=2)
        self.endDateLabel.grid(row=0, column=3)
        self.endDate.grid(row=0, column=4)
        self.startDate2Label.grid(row=1, column=1)
        self.startDate2.grid(row=1, column=2)
        self.endDate2Label.grid(row=1, column=3)
        self.endDate2.grid(row=1, column=4)
        self.loadFileBtn.grid(row=0, column=5, rowspan=2)
        self.mainFrame.grid(row=0, column=1)

    def locationAnalysisTab(self):
        self.mainFrame.grid_forget()
        self.gridForget()

        self.startDateLabel.grid(row=0, column=1)
        self.startDate.grid(row=0, column=2)
        self.endDateLabel.grid(row=0, column=3)
        self.endDate.grid(row=0, column=4)
        self.locationLabel.grid(row=1, column=3)

        #call function to load data in location.
        self.location.grid(row=1, column=4)
        self.loadFileBtn.grid(row=0, column=5, rowspan=2)
        self.mainFrame.grid(row=0, column=1)

    def gridForget(self):
        for widgets in self.mainFrame.winfo_children():
            widgets.grid_forget()

app = MainApp()
