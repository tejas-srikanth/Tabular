from tkinter import *
from tkinter.filedialog import askopenfilename
from time import *
from random import *
import os
from face_cropper import *
from pynput.keyboard import Listener, Key, Controller

WIDTH, HEIGHT = 400, 600
FONT = ("Segoe UI Bold", 14)
FONT_SECONDARY = ("Segoe UI", 14)
FONT_TITLE = ("Segoe UI", 28)
COLOUR_BACKGROUND = "#181818"
COLOUR_PRIMARY = "white"
COLOUR_SECONDARY = "#444"
COLOUR_ACCENT = "#ecb100"

screen, currFile, root = "", "", ""
recorded = [Key.alt_l, Key.tab]
recordedText = ""
keyboard = Controller()

def main():
    global screen, currFile, root
    if root != "":
        if root.state() == "normal":
            root.focus()
        else:
            init_root()
    else:
        init_root()

def on_closing():
    global root
    root.destroy()
    root = ""

def init_root():
    global screen, currFile, root
    root = Tk()
    root.title("Customize Tabular")
    root.iconbitmap(os.path.join(os.path.dirname(__file__), "sketch.ico"))
    screen = Canvas(root, width=WIDTH, height=HEIGHT,
                    background=COLOUR_BACKGROUND)
    screen.pack()
    root.resizable(0, 0)
    currFile = ""
    root.after(0, frontPage)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    screen.pack()
    screen.focus_set()
    root.mainloop()

def popupmsg(msg):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg, font=FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()

def getFile():
    global screen, currFile, root
    filename = askopenfilename()
    if filename.endswith("png") or filename.endswith("jpg"):
        currFile = filename
    else:
        currFile = False

    if not currFile:
        badText = screen.create_text(
        40, 250, text="Not a valid file", font=FONT_SECONDARY, fill="red", anchor=NW,
        width=320)
        screen.update()
        sleep(2)
        screen.delete(badText)
        # root.after(2, frontPage)
    else:
        try:
            raw = r'{}'.format(filename)
            x = crop(raw)
            screen.create_text(
                40, 250, text=filename, font=FONT_SECONDARY, fill=COLOUR_ACCENT, anchor=NW,
                width=320)
        except Exception as e:
            popupmsg(e)


def log_keystroke(key):

    if key == Key.esc:
        return False

    recorded.append(key)

def recordKeybind():
    global recorded, recordedText, keyboard
    recorded = []
    with Listener(on_press=log_keystroke) as l:
        l.join()
    screen.delete(recordedText)
    temp = []
    for x in range(len(recorded)):
        if str(recorded[x])[:4] == "Key.":
            temp.append(str(recorded[x])[4:])
        else:
            temp.append(str(recorded[x]))
    recordedText = screen.create_text(
        40, 470, text=temp, font=FONT_SECONDARY, fill=COLOUR_ACCENT, anchor=NW,
        width=320)

def frontPage():
    global screen, currFile, root, recordedText
    titleText = screen.create_text(
        40, 50, text="Customize", font=FONT_TITLE, fill=COLOUR_PRIMARY, anchor=NW)

    chooseFile = Button(root, text="CHOOSE AN IMAGE",
                        command=getFile, bg=COLOUR_SECONDARY, fg=COLOUR_PRIMARY, bd=0, font=FONT,
                        width=30, pady=15)
    chooseFile.pack()
    chooseFile.place(x=WIDTH/2, y=200, anchor=CENTER)

    recordButton = Button(root, text="SET KEYBIND",
                          command=recordKeybind, bg=COLOUR_SECONDARY, fg=COLOUR_PRIMARY, bd=0, font=FONT,
                          width=30, pady=15)
    recordButton.pack()
    recordButton.place(x=WIDTH/2, y=400, anchor=CENTER)
    recordedText = screen.create_text(
        40, 470, text="alt_l tab", font=FONT_SECONDARY, fill=COLOUR_ACCENT, anchor=NW,
        width=320)