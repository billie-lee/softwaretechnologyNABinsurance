from tkinter import filedialog as fd
from tkinter.constants import END

def selectFile():
    import app
    app.fileName.config(state="normal")
    app.fileName.delete(0, END)
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    print(filename)
    app.fileName.insert(0, filename)
    app.fileName.config(state="readonly")