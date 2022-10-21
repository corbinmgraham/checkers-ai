import tkinter
from tkinter import *

class Interface(Canvas):
    face = tkinter.Tk()

    def __init__(self):
        self.face.minsize(250, 350)
        Canvas.__init__(self, self.face, bg="grey", height=250, width=250)
        self.face.mainloop()