import tkinter as tk
from tkinter import ttk
from os import path
from tkinter import filedialog as fd

fDir = path.dirname(path.abspath(__file__))
#netDir = fDir + '\\Backup'


class Merger:

    def __init__(self, master):
        self.win = master
        self.win.title("Aggregating Tracking Numbers")
        self.create_widgets()

    def create_widgets(self):
        selFilesFrame = ttk.LabelFrame(self.win,
                                       text='Select Files: ')
        selFilesFrame.grid(column=0, row=0, sticky='NSWE',
                           padx=10, pady=5)

        def getFileName():
            print('hello from getFileName')
            fName = fd.askopenfilename(parent=self.win,
                                       initialdir=fDir)
            print("fName: " + fName)
            self.fileEntry.delete(0, tk.END)
            self.fileEntry.insert(0, fName)
            self.fileEntry.config(width=len(fName) + 3)

        lb = ttk.Button(selFilesFrame,
                        text="Browse to File...",
                        command=getFileName)
        lb.grid(column=0, row=0, sticky=tk.W)

        file = tk.StringVar()
        self.entryLen = 40
        self.fileEntry = ttk.Entry(selFilesFrame, width=self.entryLen,
                                   textvariable=file)
        self.fileEntry.bind("<Return>", lambda event: copyFile())
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)

        logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(selFilesFrame, width=self.entryLen,
                                   textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W)

        def copyFile():
            import shutil
            src = self.fileEntry.get()
            print('hello from copyFile')

        cb = ttk.Button(selFilesFrame, text="Copy File To: ",
                        command=copyFile)
        cb.grid(column=0, row=1, sticky=tk.E)

        # Add some space around each Label
        for child in selFilesFrame.winfo_children():
            child.grid_configure(padx=6, pady=6)


def main():
    root = tk.Tk()
    merger = Merger(root)
    root.mainloop()


if __name__ == "__main__":
    main()
