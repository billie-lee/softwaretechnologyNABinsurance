import os
import tkinter as tk
from tkinter import Button, Canvas, Entry, Label, Scrollbar, ttk, Frame, filedialog
from tkcalendar import DateEntry
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter.constants import BOTH, BOTTOM, END, FALSE, HORIZONTAL, LEFT, NE, NSEW, RIGHT, VERTICAL, X, Y
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from functions import fetchData, fetchLocation
from crash_analysis import Crash_Analysis

dirname = os.path.dirname(__file__)

class MainApp():

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.pack_propagate(False)
        
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
        self.logoFrame.place(x=0, y=0)

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
        
        locations = fetchLocation()

        self.location = AutocompleteCombobox(self.mainFrame, completevalues=locations)

        #call loadDataTab as it is our homescreen
        self.loadDataTab()


        #frame for loaded data
        self.loadedFrame = Frame(self.root, padx=5, pady=5)

        #widget for display below
        self.appTab = ttk.Notebook(self.loadedFrame)
        self.loadDataFrame = Frame(self.appTab, width=600)
        self.loadDateAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.timeAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.keywordAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.alcoholAnalysisFrame = Frame(self.appTab, width=600, height=400)
        self.locationAnalysisFram = Frame(self.appTab, width=600, height=400)

        self.appTab.bind("<<NotebookTabChanged>>", self.changeTab)

        self.loadDataFrame.grid(row=0, column=0)

        trv = ttk.Treeview(self.loadDataFrame, selectmode ='browse')
        
        hsb = ttk.Scrollbar(self.loadDataFrame, orient=HORIZONTAL, command=trv.xview)  
        hsb.grid(row=1, column=0, sticky=NSEW)

        vsb = ttk.Scrollbar(self.loadDataFrame, orient=VERTICAL, command=trv.yview)  
        vsb.grid(row=0, column=1, sticky=NSEW)

        trv.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        trv.grid(row=0, column=0)
        self.treeViewColumnsTest(trv)
        self.loadTreeViewData(trv)
        self.loadDateAnalysisFrame.grid(row=0, column=0)

        self.timeAnalysisFrame.grid(row=0, column=0)

        self.keywordAnalysisFrame.grid(row=0, column=0)

        self.alcoholAnalysisFrame.grid(row=0, column=0)

        self.locationAnalysisFram.grid(row=0, column=0)
        
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

        # for row in range(row_count):
        #     self.mainFrame.grid_rowconfigure(row, weight=50)

        self.root.mainloop()

    def selectFile(self):
        self.fileName.config(state="normal")
        self.fileName.delete(0, END)
        filetypes = (
            ('text files', '*.csv'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        
        print(filename)
        self.fileName.insert(0, filename)
        self.fileName.config(state="readonly")
    
    def loadData(self, filePath):
        #call function csv to db (read data)
        filePath = self.fileName.get()
        print(filePath)

        Crash_Analysis.read_data(self, filePath)

        return 0

    def loadDateAnalysis(self):
        #call function date analysis
        return 0

    def loadTimeAnalysis(self):
        #call function time analysis
        return 0

    def loadAlcoholAnalysis(self):
        #call function time analysis
        return 0
    
    def loadLocationAnalysis(self, dates):
        #call function time analysis

        startDate = self.startDate.get_date()
        endDate = self.endDate.get_date()
        location = self.location.get()
        print(type(self.startDate.get_date()))
        print(type(self.endDate.get_date()))
        print(type(self.location.get()))

        data = Crash_Analysis.get_location_analysis(self, startDate, endDate, location)

        fig, axes = plt.subplots(1)

        axes.barh(data[0],data[1])

        canvas = FigureCanvasTkAgg(fig, self.locationAnalysisFram)

        canvas.get_tk_widget().pack()

    def loadKeywordAnalysis(self):
        #call function time analysis
        return 0

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

        self.loadFileBtn.unbind("<Button-1>")
        self.loadFileBtn.bind("<Button-1>", self.loadData)

        self.mainFrame.grid(row=0, column=1)
        self.selectFileBtn.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        self.fileNameLabel.grid(row=0, column=2)
        self.fileName.grid(row=0, column=3, columnspan=2)
        self.loadFileBtn.grid(row=0, column=5, rowspan=2)
        

    def dateAndTimeAnalysisTab(self):
        self.mainFrame.grid_forget()
        self.gridForget()

        self.loadFileBtn.unbind("<Button-1>")
        self.loadFileBtn.bind("<Button-1>", self.loadDateAnalysis)

        self.startDateLabel.grid(row=0, column=1)
        self.startDate.grid(row=0, column=2)
        self.endDateLabel.grid(row=0, column=3)
        self.endDate.grid(row=0, column=4)
        self.loadFileBtn.grid(row=0, column=5, rowspan=2)
        self.mainFrame.grid(row=0, column=1)

    def keywordAnalysisTab(self):
        self.mainFrame.grid_forget()
        self.gridForget()

        self.loadFileBtn.unbind("<Button-1>")
        self.loadFileBtn.bind("<Button-1>", self.loadKeywordAnalysis)

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

        self.loadFileBtn.unbind("<Button-1>")
        self.loadFileBtn.bind("<Button-1>", self.loadAlcoholAnalysis)

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

        self.loadFileBtn.unbind("<Button-1>")
        self.loadFileBtn.bind("<Button-1>", self.loadLocationAnalysis)

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

    def treeViewColumns(self, trv):
        # number of columns
        trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33","34","35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63")
    
        # Defining heading
        trv['show'] = 'headings'
    
        # width of columns and alignment 
        trv.column("1", width = 80, anchor ='c')
        trv.column("2", width = 80, anchor ='c')
        trv.column("3", width = 80, anchor ='c')
        trv.column("4", width = 80, anchor ='c')
        trv.column("5", width = 80, anchor ='c')
        trv.column("6", width = 80, anchor ='c')
        trv.column("7", width = 80, anchor ='c')
        trv.column("8", width = 80, anchor ='c')
        trv.column("9", width = 80, anchor ='c')
        trv.column("10", width = 80, anchor ='c')
        trv.column("11", width = 80, anchor ='c')
        trv.column("12", width = 80, anchor ='c')
        trv.column("13", width = 80, anchor ='c')
        trv.column("14", width = 80, anchor ='c')
        trv.column("15", width = 80, anchor ='c')
        trv.column("16", width = 80, anchor ='c')
        trv.column("17", width = 80, anchor ='c')
        trv.column("18", width = 80, anchor ='c')
        trv.column("19", width = 80, anchor ='c')
        trv.column("20", width = 80, anchor ='c')
        trv.column("21", width = 80, anchor ='c')
        trv.column("22", width = 80, anchor ='c')
        trv.column("23", width = 80, anchor ='c')
        trv.column("24", width = 80, anchor ='c')
        trv.column("25", width = 80, anchor ='c')
        trv.column("26", width = 80, anchor ='c')
        trv.column("27", width = 80, anchor ='c')
        trv.column("28", width = 80, anchor ='c')
        trv.column("29", width = 80, anchor ='c')
        trv.column("30", width = 80, anchor ='c')
        trv.column("31", width = 80, anchor ='c')
        trv.column("32", width = 80, anchor ='c')
        trv.column("33", width = 80, anchor ='c')
        trv.column("34", width = 80, anchor ='c')
        trv.column("35", width = 80, anchor ='c')
        trv.column("36", width = 80, anchor ='c')
        trv.column("37", width = 80, anchor ='c')
        trv.column("38", width = 80, anchor ='c')
        trv.column("39", width = 80, anchor ='c')
        trv.column("40", width = 80, anchor ='c')
        trv.column("41", width = 80, anchor ='c')
        trv.column("42", width = 80, anchor ='c')
        trv.column("43", width = 80, anchor ='c')
        trv.column("44", width = 80, anchor ='c')
        trv.column("45", width = 80, anchor ='c')
        trv.column("46", width = 80, anchor ='c')
        trv.column("47", width = 80, anchor ='c')
        trv.column("48", width = 80, anchor ='c')
        trv.column("49", width = 80, anchor ='c')
        trv.column("50", width = 80, anchor ='c')
        trv.column("51", width = 80, anchor ='c')
        trv.column("52", width = 80, anchor ='c')
        trv.column("53", width = 80, anchor ='c')
        trv.column("54", width = 80, anchor ='c')
        trv.column("55", width = 80, anchor ='c')
        trv.column("56", width = 80, anchor ='c')
        trv.column("57", width = 80, anchor ='c')
        trv.column("58", width = 80, anchor ='c')
        trv.column("59", width = 80, anchor ='c')
        trv.column("60", width = 80, anchor ='c')
        trv.column("61", width = 80, anchor ='c')
        trv.column("62", width = 80, anchor ='c')
        trv.column("63", width = 80, anchor ='c')
    
        # Headings  
        # respective columns
        trv.heading("1", text ="OBJECTID")
        trv.heading("2", text ="ACCIDENT_NO")
        trv.heading("3", text ="ABS_CODE")
        trv.heading("4", text ="ACCIDENT_STATUS")
        trv.heading("5", text ="ACCIDENT_DATE")
        trv.heading("6", text ="ACCIDENT_TIME")
        trv.heading("7", text ="ALCOHOLTIME")
        trv.heading("8", text ="ACCIDENT_TYPE")
        trv.heading("9", text ="DAY_OF_WEEK")
        trv.heading("10", text ="DCA_CODE")
        trv.heading("11", text ="HIT_RUN_FLAG")
        trv.heading("12", text ="LIGHT_CONDITION")
        trv.heading("13", text ="POLICE_ATTEND")
        trv.heading("14", text ="ROAD_GEOMETRY")
        trv.heading("15", text ="SEVERITY")
        trv.heading("16", text ="SPEED_ZONE")
        trv.heading("17", text ="RUN_OFFROAD")
        trv.heading("18", text ="NODE_ID")
        trv.heading("19", text ="LONGITUDE")
        trv.heading("20", text ="LATITUDE")
        trv.heading("21", text ="NODE_TYPE")
        trv.heading("22", text ="LGA_NAME")
        trv.heading("23", text ="REGION_NAME")
        trv.heading("24", text ="VICGRID_X")
        trv.heading("25", text ="VICGRID_Y")
        trv.heading("26", text ="TOTAL_PERSONS")
        trv.heading("27", text ="INJ_OR_FATAL")
        trv.heading("28", text ="FATALITY")
        trv.heading("29", text ="SERIOUSINJURY")
        trv.heading("30", text ="OTHERINJURY")
        trv.heading("31", text ="NONINJURED")
        trv.heading("32", text ="MALES")
        trv.heading("33", text ="FEMALES")
        trv.heading("34", text ="BICYCLIST")
        trv.heading("35", text ="PASSENGER")
        trv.heading("36", text ="DRIVER")
        trv.heading("37", text ="PEDESTRIAN")
        trv.heading("38", text ="PILLION")
        trv.heading("39", text ="MOTORIST")
        trv.heading("40", text ="UNKNOWN")
        trv.heading("41", text ="PED_CYCLIST_5_12")
        trv.heading("42", text ="PED_CYCLIST_13_18")
        trv.heading("43", text ="OLD_PEDESTRIAN")
        trv.heading("44", text ="OLD_DRIVER")
        trv.heading("45", text ="YOUNG_DRIVER")
        trv.heading("46", text ="ALCOHOL_RELATED")
        trv.heading("47", text ="UNLICENCSED")
        trv.heading("48", text ="NO_OF_VEHICLES")
        trv.heading("49", text ="HEAVYVEHICLE")
        trv.heading("50", text ="PASSENGERVEHICLE")
        trv.heading("51", text ="MOTORCYCLE")
        trv.heading("52", text ="PUBLICVEHICLE")
        trv.heading("53", text ="DEG_URBAN_NAME")
        trv.heading("54", text ="DEG_URBAN_ALL")
        trv.heading("55", text ="LGA_NAME_ALL")
        trv.heading("56", text ="REGION_NAME_ALL")
        trv.heading("57", text ="SRNS")
        trv.heading("58", text ="SRNS_ALL")
        trv.heading("59", text ="RMA")
        trv.heading("60", text ="RMA_ALL")
        trv.heading("61", text ="DIVIDED")
        trv.heading("62", text ="DIVIDED_ALL")
        trv.heading("63", text ="STAT_DIV_NAME")

    def treeViewColumnsTest(self, trv):
        # number of columns
        trv["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    
        # Defining heading
        trv['show'] = 'headings'
    
        # width of columns and alignment 
        trv.column("1", width = 80, anchor ='c')
        trv.column("2", width = 100, anchor ='c')
        trv.column("3", width = 100, anchor ='c')
        trv.column("4", width = 100, anchor ='c')
        trv.column("5", width = 100, anchor ='c')
        trv.column("6", width = 100, anchor ='c')
        trv.column("7", width = 100, anchor ='c')
        trv.column("8", width = 100, anchor ='c')
        trv.column("9", width = 100, anchor ='c')
        trv.column("10", width = 100, anchor ='c')
    
        # Headings  
        # respective columns
        trv.heading("1", text ="OBJECTID")
        trv.heading("2", text ="ACCIDENT_NO")
        trv.heading("3", text ="ABS_CODE")
        trv.heading("4", text ="ACCIDENT_STATUS")
        trv.heading("5", text ="ACCIDENT_DATE")
        trv.heading("6", text ="ACCIDENT_TIME")
        trv.heading("7", text ="ALCOHOLTIME")
        trv.heading("8", text ="ACCIDENT_TYPE")
        trv.heading("9", text ="DAY_OF_WEEK")
        trv.heading("10", text ="DCA_CODE")

    def loadTreeViewData(self, trv):
        data = fetchData()

        for dt in data: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
                values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9]))



app = MainApp()
