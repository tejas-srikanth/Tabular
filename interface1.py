from tkinter import *
from tkinter.filedialog import askopenfilename
from time import *
from random import *
from face_cropper import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")
screen.pack()

currFile = ""

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg, font="Times 12")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def getFile():
    filename = askopenfilename()
    if filename.endswith("png") or filename.endswith("jpg"):
        currFile = filename
    else:
        currFile = False

    if not currFile:
        badText = screen.create_text( 282.5, 250, text="Not valid file, please submit .jpg or .png", font="Times 12", fill="red")
        screen.update()
        sleep(0.5)
        screen.delete(badText)
        root.after(2, frontPage)
    else:
        try:
            raw = r'{}'.format(filename)
            x = crop(raw)
            screen.create_text( 282.5, 250, text=filename, font="Times 12", fill="blue")
        except Exception as e:
            popupmsg(e)
            
        
        

def frontPage():
    chooseFile = Button(root, text="Choose an image of your face", command=getFile)
    chooseFile.pack()
    chooseFile.place(x=200, y=200)

root.after(0, frontPage)

screen.pack()
screen.focus_set()
root.mainloop()




