from tkinter import Canvas, Frame, ttk
import tkinter  as tk
from tkinter.constants import BOTH, BOTTOM, HORIZONTAL, LEFT, NW, X 
from functions import fetchData

my_w = tk.Tk()
my_str = tk.StringVar() # to display query at end

def my_display(offset):

    mainFrame = Frame(my_w)
    mainFrame.pack(fill=BOTH, expand=1)

    myCanvas = Canvas(mainFrame)
    myCanvas.pack(side=LEFT, fill=BOTH, expand=1)

    myScrollbar = ttk.Scrollbar(mainFrame, orient=HORIZONTAL, command=myCanvas.xview)
    myScrollbar.pack(side=BOTTOM, fill=X)

    myCanvas.configure(xscrollcommand=myScrollbar.set)
    myCanvas.bind('<Configure>', lambda e:myCanvas.configure(scrollregion=myCanvas.bbox("all")))

    canvasFrame = Frame(myCanvas)

    myCanvas.create_window((0,0), window=canvasFrame, anchor=NW)

    ###
    trv = ttk.Treeview(canvasFrame, selectmode ='browse', xscrollcommand=myScrollbar.set)
  
    trv.grid(row=1,column=2,padx=20,pady=20,columnspan=3)
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

    ###
    data = fetchData()

    for dt in data: 
        trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9],dt[10],dt[11],dt[12],dt[13],dt[14],dt[15],dt[16],dt[17],dt[18],dt[19],dt[20],dt[21],dt[22],dt[23],dt[24],dt[25],dt[26],dt[27],dt[28],dt[29],dt[30],dt[31],dt[32],dt[33],dt[34],dt[35],dt[36],dt[37],dt[38],dt[39],dt[40],dt[41],dt[42],dt[43],dt[44],dt[45],dt[46],dt[47],dt[48],dt[49],dt[50],dt[51],dt[52],dt[53],dt[54],dt[55],dt[56],dt[57],dt[58],dt[59],dt[60],dt[61],dt[62]))

    # Show buttons 
    # back = offset - limit # This value is used by Previous button
    # next = offset + limit # This value is used by Next button       
    # b1 = tk.Button(my_w, text='< Prev', command=lambda: my_display(back))
    # b1.grid(row=2,column=2,sticky='E')
    # b2 = tk.Button(my_w, text='Next >', command=lambda: my_display(next))
    # b2.grid(row=2,column=3)

    # if(no_rec <= next): 
    #     b2["state"]="disabled" # disable next button
    # else:
    #     b2["state"]="active"  # enable next button
        
    # if(back >= 0):
    #     b1["state"]="active"  # enable Prev button
    # else:
    #     b1["state"]="disabled"# disable Prev button 

    # for your understanding of how the offset value changes
    # query is displayed here, it is not part of the script 
    # my_str.set(q + '\n' + "next: " + str(next) + "\n back:"+str(back))
    # l1 = tk.Label(my_w, textvariable=my_str)
    # l1.grid(row=3,column=1,columnspan=3)
my_display(0)        
my_w.mainloop()