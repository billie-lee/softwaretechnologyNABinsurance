import os
import tkinter as tk
import tkcalendar as tkc
from tkinter import ttk, messagebox
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter.constants import BOTTOM, BROWSE, END, HORIZONTAL, RIGHT, VERTICAL, X, Y
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import numpy as np
from crash_analysis import Crash_Analysis

def placeForget():
    for widgets in mainFrame.winfo_children():
        widgets.place_forget()

    for widgets in loadDataFrame.winfo_children():
        widgets.place_forget()

    for widgets in loadDateAnalysisFrame.winfo_children():
        widgets.place_forget()
    
    for widgets in timeAnalysisFrame.winfo_children():
        widgets.pack_forget()

    for widgets in keywordAnalysisFrame.winfo_children():
        widgets.place_forget()

    for widgets in alcoholAnalysisFrame.winfo_children():
        widgets.pack_forget()

    for widgets in locationAnalysisFram.winfo_children():
        widgets.pack_forget()

    for widgets in lowerFrame.winfo_children():
        widgets.place_forget()

def changeTab(event):
    selectedTab = event.widget.select()
    tabText = event.widget.tab(selectedTab, "text")

    if tabText == "Load Data":
        loadDataTab()
    elif tabText == "Date Analysis":
        dateAnalysisTab()
    elif tabText == "Time Analysis":
        timeAnalysisTab()
    elif tabText == "Keyword Analysis":
        keywordAnalysisTab()
    elif tabText == "Alcohol Analysis":
        alcoholAnalysisTab()
    elif tabText == "Location Analysis":
        locationAnalysisTab()

def loadData(filePath):
    #call function csv to db (read data)
    filePath = fileName.get()
    print(filePath)

    data = Crash_Analysis()
    result = data.read_data(filePath)

    messagebox.showinfo('information', result)

    loadDataTab()

def loadDateAnalysis(data):
    #call function date analysis
    frame1 = tk.Frame(loadDateAnalysisFrame)
    frame1.place(height=390, width=705, rely=0, relx=0)

    tv1 = ttk.Treeview(frame1, selectmode=BROWSE)
    tv1.place(relheight=1, relwidth=1)

    hsb = tk.Scrollbar(frame1, orient=HORIZONTAL, command=tv1.xview)
    vsb = tk.Scrollbar(frame1, orient=VERTICAL, command=tv1.yview)

    tv1.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
    hsb.pack(side=BOTTOM, fill=X)
    vsb.pack(side=RIGHT, fill=Y)

    treeviewColumn(tv1)

    sd = startDate.get_date()
    ed = endDate.get_date()

    print(sd, ed)

    data = Crash_Analysis()
    result = data.get_period(sd, ed)

    loadTreeviewData(tv1, result)

    for widgets in lowerFrame.winfo_children():
        widgets.place_forget()
    
    RowLabel = tk.Label(lowerFrame, text=f"Number of Data: {len(result)}")
    RowLabel.place(height=50, width=850, relheight=0)


def loadTimeAnalysis(data):
    #call function time analysis
    for widgets in timeAnalysisFrame.winfo_children():
        widgets.pack_forget()
    
    fig, axes = plt.subplots(1)

    sd = startDate.get_date()
    ed = endDate.get_date()

    print(sd, ed)

    data = Crash_Analysis()

    result = data.get_time_analysis(sd, ed)

    axes.plot(result[0],result[1], marker=11)
    axes.set_xlabel("Hours")
    axes.set_ylabel("Number of Accidents")

    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, timeAnalysisFrame)

    canvas.get_tk_widget().pack()

    root.update()

    for widgets in lowerFrame.winfo_children():
        widgets.place_forget()

    RowLabel = tk.Label(lowerFrame, text=f"Number of Accidents: {sum(result[1])}")
    RowLabel.place(height=50, width=850, relheight=0)

def loadKeywordAnalysis(data):
    #call function time analysis
    frame1 = tk.Frame(keywordAnalysisFrame)
    frame1.place(height=390, width=705, rely=0, relx=0)

    tv1 = ttk.Treeview(frame1, selectmode=BROWSE)
    tv1.place(relheight=1, relwidth=1)

    hsb = tk.Scrollbar(frame1, orient=HORIZONTAL, command=tv1.xview)
    vsb = tk.Scrollbar(frame1, orient=VERTICAL, command=tv1.yview)

    tv1.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
    hsb.pack(side=BOTTOM, fill=X)
    vsb.pack(side=RIGHT, fill=Y)

    treeviewColumn(tv1)

    sd = startDate.get_date()
    ed = endDate.get_date()
    kw = keyword.get()

    print(sd, ed, kw)

    data = Crash_Analysis()
    result = data.get_keyword(sd, ed, kw)

    loadTreeviewData(tv1, result)

    for widgets in lowerFrame.winfo_children():
        widgets.place_forget()

    RowLabel = tk.Label(lowerFrame, text=f"Number of Data: {len(result)}")
    RowLabel.place(height=50, width=850, relheight=0)

def loadAlcoholAnalysis(data):
    #call function time analysis
    for widgets in alcoholAnalysisFrame.winfo_children():
        widgets.pack_forget()
    
    sd = startDate.get_date()
    ed = endDate.get_date()
    sd2 = startDate2.get_date()
    ed2 = endDate2.get_date()

    print(sd, ed, sd2, ed2)

    data = Crash_Analysis()

    result = data.get_alcohol_analysis(sd, ed, sd2, ed2)
    
    X_axis = np.arange(len(result[0][0]))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.bar(X_axis - 0.2, result[0][1], 0.4, label = '1st Period')
    plt.bar(X_axis + 0.2, result[1][1], 0.4, label = '2nd Period')
    
    plt.xticks(X_axis, result[0][0])
    plt.xlabel("Accident Types")
    plt.ylabel("Number of Accidents")
    plt.legend()

    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.tight_layout()
    plt.xticks(fontsize=8)

    canvas = FigureCanvasTkAgg(fig, alcoholAnalysisFrame)

    canvas.get_tk_widget().pack()

    root.update()

    for widgets in lowerFrame.winfo_children():
        widgets.place_forget()

    RowLabel = tk.Label(lowerFrame, text=f"Number of Accidents for Period 1: {sum(result[0][1])} and Period 2: {sum(result[1][1])}")
    RowLabel.place(height=50, width=850, relheight=0)

def loadLocationAnalysis(data):
    #call function time analysis
    for widgets in locationAnalysisFram.winfo_children():
        widgets.pack_forget()
    
    fig, axes = plt.subplots(1)

    sd = startDate.get_date()
    ed = endDate.get_date()
    lo = location.get()

    print(sd, ed,lo)

    data = Crash_Analysis()

    result = data.get_location_analysis(sd, ed, lo)

    axes.bar(result[0],result[1])
    axes.set_ylabel("Number of Accidents")
    axes.set_xlabel("Accident Type")

    plt.setp(axes.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.tight_layout()
    plt.xticks(fontsize=8)

    canvas = FigureCanvasTkAgg(fig, locationAnalysisFram)

    canvas.get_tk_widget().pack()

    root.update()

    for widgets in lowerFrame.winfo_children():
        widgets.place_forget()

    RowLabel = tk.Label(lowerFrame, text=f"Number of Accidents: {sum(result[1])}")
    RowLabel.place(height=50, width=850, relheight=0)

def selectFile():
    fileName.delete(0, END)
    filetypes = (
            ('text files', '*.csv'),
            ('All files', '*.*')
    )

    filename = tk.filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

    fileName.insert(0, filename)

def loadDataTab():
    mainFrame.place_forget()
    placeForget()

    loadFileBtn.unbind("<Button-1>")
    loadFileBtn.bind("<Button-1>", loadData)

    mainFrame.place(height=80, width=850, rely=0, relx=0)
    selectFileBtn.place(rely=0.2, relx=0.2)
    fileNameLabel.place(rely=0.2, relx=0.35)
    fileName.place(rely=0.2, relx=0.5)

    loadFileBtn.place(rely=0.15, relx=0.85)

    frame1 = tk.Frame(loadDataFrame)
    frame1.place(height=390, width=705, rely=0, relx=0)

    tv1 = ttk.Treeview(frame1, selectmode=BROWSE)
    tv1.place(relheight=1, relwidth=1)

    hsb = tk.Scrollbar(frame1, orient=HORIZONTAL, command=tv1.xview)
    vsb = tk.Scrollbar(frame1, orient=VERTICAL, command=tv1.yview)

    tv1.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
    hsb.pack(side=BOTTOM, fill=X)
    vsb.pack(side=RIGHT, fill=Y)

    treeviewColumn(tv1)

    data = Crash_Analysis()
    result = data.load_data()

    loadTreeviewData(tv1, result)

    lowerFrame.place(height=50, width=850, rely=0.9, relx=0)

    RowLabel = tk.Label(lowerFrame, text=f"Number of Data: {len(result)}")
    RowLabel.place(height=50, width=850, relheight=0)

def dateAnalysisTab():
    mainFrame.place_forget()
    placeForget()

    loadFileBtn.unbind("<Button-1>")
    loadFileBtn.bind("<Button-1>", loadDateAnalysis)

    mainFrame.place(height=80, width=850, rely=0, relx=0)

    startDateLabel.place(rely=.2, relx=0.2)
    startDate.place(rely=.2, relx=0.3)
    endDateLabel.place(rely=.2, relx=0.5)
    endDate.place(rely=.2, relx=0.6)

    loadFileBtn.place(rely=.15, relx=0.85)

    lowerFrame.place(height=50, width=850, rely=0.9, relx=0)

    RowLabel = tk.Label(lowerFrame, text="Number of Data:")
    RowLabel.place(height=50, width=850, relheight=0)

def timeAnalysisTab():
    mainFrame.place_forget()
    placeForget()

    loadFileBtn.unbind("<Button-1>")
    loadFileBtn.bind("<Button-1>", loadTimeAnalysis)

    mainFrame.place(height=80, width=850, rely=0, relx=0)

    startDateLabel.place(rely=0.2, relx=0.2)
    startDate.place(rely=0.2, relx=0.3)
    endDateLabel.place(rely=0.2, relx=0.5)
    endDate.place(rely=0.2, relx=0.6)

    loadFileBtn.place(rely=0.15, relx=0.85)

    lowerFrame.place(height=50, width=850, rely=0.9, relx=0)

    RowLabel = tk.Label(lowerFrame, text="Number of Accidents:")
    RowLabel.place(height=50, width=850, relheight=0)

def keywordAnalysisTab():
    mainFrame.place_forget()
    placeForget()

    loadFileBtn.unbind("<Button-1>")
    loadFileBtn.bind("<Button-1>", loadKeywordAnalysis)

    mainFrame.place(height=80, width=850, rely=0, relx=0)

    startDateLabel.place(rely=0.2, relx=0.2)
    startDate.place(rely=0.2, relx=0.3)
    endDateLabel.place(rely=0.2, relx=0.5)
    endDate.place(rely=0.2, relx=0.6)

    keywordLabel.place(rely=0.6, relx=0.5)
    keyword.place(rely=0.6, relx=0.6)

    loadFileBtn.place(rely=0.15, relx=0.85)

    lowerFrame.place(height=50, width=850, rely=0.9, relx=0)


    RowLabel = tk.Label(lowerFrame, text="Number of Data:")
    RowLabel.place(height=50, width=850, relheight=0)

def alcoholAnalysisTab():
    mainFrame.place_forget()
    placeForget()

    loadFileBtn.unbind("<Button-1>")
    loadFileBtn.bind("<Button-1>", loadAlcoholAnalysis)

    mainFrame.place(height=80, width=850, rely=0, relx=0)

    startDateLabel.place(rely=0.2, relx=0.2)
    startDate.place(rely=0.2, relx=0.3)
    endDateLabel.place(rely=0.2, relx=0.5)
    endDate.place(rely=0.2, relx=0.6)

    startDate2Label.place(rely=0.6, relx=0.2)
    startDate2.place(rely=0.6, relx=0.3)
    endDate2Label.place(rely=0.6, relx=0.5)
    endDate2.place(rely=0.6, relx=0.6)

    loadFileBtn.place(rely=0.15, relx=0.85)

    lowerFrame.place(height=50, width=850, rely=0.9, relx=0)

    RowLabel = tk.Label(lowerFrame, text="Number of Accidents for Period 1: and Period 2:")
    RowLabel.place(height=50, width=850, relheight=0)

def locationAnalysisTab():
    mainFrame.place_forget()
    placeForget()

    loadFileBtn.unbind("<Button-1>")
    loadFileBtn.bind("<Button-1>", loadLocationAnalysis)

    mainFrame.place(height=80, width=850, rely=0, relx=0)

    startDateLabel.place(rely=0.2, relx=0.2)
    startDate.place(rely=0.2, relx=0.3)
    endDateLabel.place(rely=0.2, relx=0.5)
    endDate.place(rely=0.2, relx=0.6)

    data = Crash_Analysis()
    locations = data.fetch_location()
    location['values'] = locations

    locationLabel.place(rely=0.6, relx=0.5)
    location.place(rely=0.6, relx=0.6)

    loadFileBtn.place(rely=0.15, relx=0.85)

    lowerFrame.place(height=50, width=850, rely=0.9, relx=0)

    RowLabel = tk.Label(lowerFrame, text="Number of Accidents:")
    RowLabel.place(height=50, width=850, relheight=0)

def treeviewColumn(tv1):
    tv1["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33","34","35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63")

    tv1['show'] = 'headings'

    # width of columns and alignment 
    tv1.column("1", width = 80, anchor ='c')
    tv1.column("2", width = 80, anchor ='c')
    tv1.column("3", width = 80, anchor ='c')
    tv1.column("4", width = 80, anchor ='c')
    tv1.column("5", width = 80, anchor ='c')
    tv1.column("6", width = 80, anchor ='c')
    tv1.column("7", width = 80, anchor ='c')
    tv1.column("8", width = 80, anchor ='c')
    tv1.column("9", width = 80, anchor ='c')
    tv1.column("10", width = 80, anchor ='c')
    tv1.column("11", width = 80, anchor ='c')
    tv1.column("12", width = 80, anchor ='c')
    tv1.column("13", width = 80, anchor ='c')
    tv1.column("14", width = 80, anchor ='c')
    tv1.column("15", width = 80, anchor ='c')
    tv1.column("16", width = 80, anchor ='c')
    tv1.column("17", width = 80, anchor ='c')
    tv1.column("18", width = 80, anchor ='c')
    tv1.column("19", width = 80, anchor ='c')
    tv1.column("20", width = 80, anchor ='c')
    tv1.column("21", width = 80, anchor ='c')
    tv1.column("22", width = 80, anchor ='c')
    tv1.column("23", width = 80, anchor ='c')
    tv1.column("24", width = 80, anchor ='c')
    tv1.column("25", width = 80, anchor ='c')
    tv1.column("26", width = 80, anchor ='c')
    tv1.column("27", width = 80, anchor ='c')
    tv1.column("28", width = 80, anchor ='c')
    tv1.column("29", width = 80, anchor ='c')
    tv1.column("30", width = 80, anchor ='c')
    tv1.column("31", width = 80, anchor ='c')
    tv1.column("32", width = 80, anchor ='c')
    tv1.column("33", width = 80, anchor ='c')
    tv1.column("34", width = 80, anchor ='c')
    tv1.column("35", width = 80, anchor ='c')
    tv1.column("36", width = 80, anchor ='c')
    tv1.column("37", width = 80, anchor ='c')
    tv1.column("38", width = 80, anchor ='c')
    tv1.column("39", width = 80, anchor ='c')
    tv1.column("40", width = 80, anchor ='c')
    tv1.column("41", width = 80, anchor ='c')
    tv1.column("42", width = 80, anchor ='c')
    tv1.column("43", width = 80, anchor ='c')
    tv1.column("44", width = 80, anchor ='c')
    tv1.column("45", width = 80, anchor ='c')
    tv1.column("46", width = 80, anchor ='c')
    tv1.column("47", width = 80, anchor ='c')
    tv1.column("48", width = 80, anchor ='c')
    tv1.column("49", width = 80, anchor ='c')
    tv1.column("50", width = 80, anchor ='c')
    tv1.column("51", width = 80, anchor ='c')
    tv1.column("52", width = 80, anchor ='c')
    tv1.column("53", width = 80, anchor ='c')
    tv1.column("54", width = 80, anchor ='c')
    tv1.column("55", width = 80, anchor ='c')
    tv1.column("56", width = 80, anchor ='c')
    tv1.column("57", width = 80, anchor ='c')
    tv1.column("58", width = 80, anchor ='c')
    tv1.column("59", width = 80, anchor ='c')
    tv1.column("60", width = 80, anchor ='c')
    tv1.column("61", width = 80, anchor ='c')
    tv1.column("62", width = 80, anchor ='c')
    tv1.column("63", width = 80, anchor ='c')

    # respective columns
    tv1.heading("1", text ="OBJECTID")
    tv1.heading("2", text ="ACCIDENT_NO")
    tv1.heading("3", text ="ABS_CODE")
    tv1.heading("4", text ="ACCIDENT_STATUS")
    tv1.heading("5", text ="ACCIDENT_DATE")
    tv1.heading("6", text ="ACCIDENT_TIME")
    tv1.heading("7", text ="ALCOHOLTIME")
    tv1.heading("8", text ="ACCIDENT_TYPE")
    tv1.heading("9", text ="DAY_OF_WEEK")
    tv1.heading("10", text ="DCA_CODE")
    tv1.heading("11", text ="HIT_RUN_FLAG")
    tv1.heading("12", text ="LIGHT_CONDITION")
    tv1.heading("13", text ="POLICE_ATTEND")
    tv1.heading("14", text ="ROAD_GEOMETRY")
    tv1.heading("15", text ="SEVERITY")
    tv1.heading("16", text ="SPEED_ZONE")
    tv1.heading("17", text ="RUN_OFFROAD")
    tv1.heading("18", text ="NODE_ID")
    tv1.heading("19", text ="LONGITUDE")
    tv1.heading("20", text ="LATITUDE")
    tv1.heading("21", text ="NODE_TYPE")
    tv1.heading("22", text ="LGA_NAME")
    tv1.heading("23", text ="REGION_NAME")
    tv1.heading("24", text ="VICGRID_X")
    tv1.heading("25", text ="VICGRID_Y")
    tv1.heading("26", text ="TOTAL_PERSONS")
    tv1.heading("27", text ="INJ_OR_FATAL")
    tv1.heading("28", text ="FATALITY")
    tv1.heading("29", text ="SERIOUSINJURY")
    tv1.heading("30", text ="OTHERINJURY")
    tv1.heading("31", text ="NONINJURED")
    tv1.heading("32", text ="MALES")
    tv1.heading("33", text ="FEMALES")
    tv1.heading("34", text ="BICYCLIST")
    tv1.heading("35", text ="PASSENGER")
    tv1.heading("36", text ="DRIVER")
    tv1.heading("37", text ="PEDESTRIAN")
    tv1.heading("38", text ="PILLION")
    tv1.heading("39", text ="MOTORIST")
    tv1.heading("40", text ="UNKNOWN")
    tv1.heading("41", text ="PED_CYCLIST_5_12")
    tv1.heading("42", text ="PED_CYCLIST_13_18")
    tv1.heading("43", text ="OLD_PEDESTRIAN")
    tv1.heading("44", text ="OLD_DRIVER")
    tv1.heading("45", text ="YOUNG_DRIVER")
    tv1.heading("46", text ="ALCOHOL_RELATED")
    tv1.heading("47", text ="UNLICENCSED")
    tv1.heading("48", text ="NO_OF_VEHICLES")
    tv1.heading("49", text ="HEAVYVEHICLE")
    tv1.heading("50", text ="PASSENGERVEHICLE")
    tv1.heading("51", text ="MOTORCYCLE")
    tv1.heading("52", text ="PUBLICVEHICLE")
    tv1.heading("53", text ="DEG_URBAN_NAME")
    tv1.heading("54", text ="DEG_URBAN_ALL")
    tv1.heading("55", text ="LGA_NAME_ALL")
    tv1.heading("56", text ="REGION_NAME_ALL")
    tv1.heading("57", text ="SRNS")
    tv1.heading("58", text ="SRNS_ALL")
    tv1.heading("59", text ="RMA")
    tv1.heading("60", text ="RMA_ALL")
    tv1.heading("61", text ="DIVIDED")
    tv1.heading("62", text ="DIVIDED_ALL")
    tv1.heading("63", text ="STAT_DIV_NAME")

def loadTreeviewData(tv1, data):
    
    for index, dt in enumerate(data): 
        if index % 2:
            tv1.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],
            dt[10],dt[11],dt[12],dt[13],dt[14],dt[15],dt[16],dt[17],dt[18],dt[19],
            dt[20],dt[21],dt[22],dt[23],dt[24],dt[25],dt[26],dt[27],dt[28],dt[29],
            dt[30],dt[31],dt[32],dt[33],dt[34],dt[35],dt[36],dt[37],dt[38],dt[39],
            dt[40],dt[41],dt[42],dt[43],dt[44],dt[45],dt[46],dt[47],dt[48],dt[49],
            dt[50],dt[51],dt[52],dt[53],dt[54],dt[55],dt[56],dt[57],dt[58],dt[59],
            dt[60],dt[61],dt[62]))
        else:
            tv1.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],
            dt[10],dt[11],dt[12],dt[13],dt[14],dt[15],dt[16],dt[17],dt[18],dt[19],
            dt[20],dt[21],dt[22],dt[23],dt[24],dt[25],dt[26],dt[27],dt[28],dt[29],
            dt[30],dt[31],dt[32],dt[33],dt[34],dt[35],dt[36],dt[37],dt[38],dt[39],
            dt[40],dt[41],dt[42],dt[43],dt[44],dt[45],dt[46],dt[47],dt[48],dt[49],
            dt[50],dt[51],dt[52],dt[53],dt[54],dt[55],dt[56],dt[57],dt[58],dt[59],
            dt[60],dt[61],dt[62]), tag="gray")
    tv1.tag_configure("gray", background="#cccccc")


dirname = os.path.dirname(__file__)
root = tk.Tk()

root.geometry("850x600")
root.pack_propagate(False)
root.resizable(0,0)
root.title("NAB Insurance")

#frame for main menu
mainFrame = tk.Frame(root, padx=5, pady=5)
logoFrame = tk.Frame(root, padx=5, pady=5)

#canvas for logo
logoCanvas = tk.Canvas(logoFrame, width=100, height=50)
logo = Image.open(dirname+"/images/logo.png").resize((120, 70), Image.ANTIALIAS)
#resized logo
resizedLogo= ImageTk.PhotoImage(logo)
logoCanvas.create_image(50,20, image=resizedLogo)
logoCanvas.grid(row=0, column=0)
logoFrame.place(height=50, width=100, rely=0.03, relx=0.01)


#initialize widgets for main menu
#widgets for load data tab
fileNameLabel = tk.Label(mainFrame, text="File Name:")
fileName = tk.Entry(mainFrame)

selectFileBtn = tk.Button(mainFrame, text="SELECT FILE", command=selectFile, width=10)
loadFileBtn = tk.Button(mainFrame, text="Load", width=10, height=3)

#widgets for Date and Time Analysis
startDateLabel = tk.Label(mainFrame, text="Start Date:*")
startDate = tkc.DateEntry(mainFrame, selectmode="day")
endDateLabel = tk.Label(mainFrame, text="End Date:*")
endDate = tkc.DateEntry(mainFrame, selectmode="day")

#additional widgets for Keyword Analysis
keywordLabel = tk.Label(mainFrame, text="Keyword:")
keyword = tk.Entry(mainFrame)

#additional widgets for Alcohol Analysis
startDate2Label = tk.Label(mainFrame, text="Start Date:")
startDate2 = tkc.DateEntry(mainFrame, selectmode="day")
endDate2Label = tk.Label(mainFrame, text="End Date:")
endDate2 = tkc.DateEntry(mainFrame, selectmode="day")

#additional widgets for Location Analysis
locationLabel = tk.Label(mainFrame, text="Location:")



location = AutocompleteCombobox(mainFrame, completedvalues=None)

loadedFrame = tk.Frame(root)
loadedFrame.place(height=450, width=800, rely=0.15, relx=0)

#widget for display below
appTab = ttk.Notebook(loadedFrame)
loadDataFrame = tk.Frame(appTab)
loadDateAnalysisFrame = tk.Frame(appTab)
timeAnalysisFrame = tk.Frame(appTab)
keywordAnalysisFrame = tk.Frame(appTab)
alcoholAnalysisFrame = tk.Frame(appTab)
locationAnalysisFram = tk.Frame(appTab)

appTab.add(loadDataFrame, text="Load Data")
appTab.add(loadDateAnalysisFrame, text="Date Analysis")
appTab.add(timeAnalysisFrame, text="Time Analysis")
appTab.add(keywordAnalysisFrame, text="Keyword Analysis")
appTab.add(alcoholAnalysisFrame, text="Alcohol Analysis")
appTab.add(locationAnalysisFram, text="Location Analysis")

appTab.pack(side=RIGHT, fill=Y)

appTab.bind("<<NotebookTabChanged>>", changeTab)

lowerFrame = tk.Frame(root, padx=5, pady=5)



loadDataTab()

root.mainloop()