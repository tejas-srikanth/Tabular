from tkinter import *
from tkinter.filedialog import askopenfilename
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")
screen.pack()

currFile = ""

def getFile():
    filename = askopenfilename()
    if filename.endswith("png") or filename.endswith("jpg"):
        currFile = filename
    else:
        currFile = False

    if not currFile:
        badText = screen.create_text( 282.5, 350, text="Not valid file, please submit .jpg or .png", font="Times 12", fill="red")
        screen.update()
        sleep(0.5)
        screen.delete(badText)
        root.after(2, frontPage)
    else:
        screen.create_text( 282.5, 350, text=filename, font="Times 12", fill="blue")
        
        

def frontPage():
    chooseFile = Button(root, text="Choose an image of your face", command=getFile)
    chooseFile.pack()
    chooseFile.place(x=200, y=300)

root.after(0, frontPage)

screen.pack()
screen.focus_set()
root.mainloop()




