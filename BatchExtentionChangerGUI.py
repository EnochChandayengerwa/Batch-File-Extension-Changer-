# Batch File Extention Name Changer GUI

from tkinter import Canvas, font, filedialog
import sys, os
import tkinter as tk

# Global variables
folderPath = ""
oldExt = ""
newExt = ""

# Get Path
def getPath():
    global folderPath
    folderPath = filedialog.askdirectory()
    if os.path.isdir(folderPath):
        label1.config(text=folderPath)
        

# File Proccessing
def processFiles():
    global folderPath, oldExt, newExt
    dirr = folderPath
    oldExt = oldExtTf.get("1.0","end-1c")
    newExt = newExtTf.get("1.0","end-1c")
    for i in os.listdir(dirr):
        files = os.path.join(dirr,i)
        split= os.path.splitext(files)
        if split[1]==oldExt:
            os.rename(files,split[0]+newExt)
            
# Main Window
root = tk.Tk()
canvas = tk.Canvas(root, width=400,height=160)
canvas.pack()

# Lables
label1 = tk.Label(root,text="Folder Path...")
label1.config(font=("TkDefaultFont"),justify="center", wraplength=250)
label1.pack()
canvas.create_window(260,40, window=label1)

lblfrom = tk.Label(root, text="From")
lblfrom.pack()
canvas.create_window(120,90,window=lblfrom)

lblto = tk.Label(root, text="To")
lblto.pack()
canvas.create_window(200,90,window=lblto)

# Buttons
browseBtn = tk.Button(text="    Select Folder   ",font="TkDefaultFont",command=getPath)
canvas.create_window(90,40,window=browseBtn)

changeBtn = tk.Button(text="    Change   ",font="TkDefaultFont",fg="green", command=processFiles)
canvas.create_window(200,130,window=changeBtn)

# Text Fields
oldExtTf = tk.Text(root,height = 1, width = 5)
oldExtTf.pack()
canvas.create_window(165,90,window=oldExtTf)

newExtTf = tk.Text(root,height = 1, width = 5)
newExtTf.pack()
canvas.create_window(235,90,window=newExtTf)


# Main
if __name__ == "__main__":
    #processFiles()
    root.title("Batch File Extention Name Changer")
    root.eval("tk::PlaceWindow . center")
    root.resizable(width=False,height=False)
    root.mainloop()
