import os
from tkinter import filedialog as fd
from tkinter import Button, Canvas, Entry, Label, PhotoImage, StringVar, Tk
from tkinter.constants import END
from PIL import ImageTk, Image

dirname = os.path.dirname(__file__)

def selectFile():
    fileName.config(state="normal")
    fileName.delete(0, END)
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    print(filename)
    fileName.insert(0, filename)
    fileName.config(state="readonly")

#main app
root = Tk()
root.title("NAB Insurance")
root.geometry("600x400")

#canvas for logo
logoCanvas = Canvas(root, width=100, height=50)
logo = Image.open(dirname+"/images/logo.png").resize((100, 50), Image.ANTIALIAS)
#resized logo
resizedLogo= ImageTk.PhotoImage(logo)
logoCanvas.create_image(50,20, image=resizedLogo)

fileNameLabel = Label(root, text="File Name:")
fileName = Entry(root)
fileName.config(state="readonly")

selectFileBtn = Button(root, text="SELECT FILE", command=selectFile)
loadFileBtn = Button(root, text="Load", width=5, height=3)

#adding widgets to screen
logoCanvas.grid(row=0, column=0)
selectFileBtn.grid(row=0, column=1)
fileNameLabel.grid(row=0, column=2)
fileName.grid(row=0, column=3)
loadFileBtn.grid(row=0, column=4)

root.mainloop()