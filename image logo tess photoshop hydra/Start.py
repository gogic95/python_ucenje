#  Copyright (c) Filip Gogic 2022.
import time
from tkinter import *

import guimainclass

root = Tk()
form = guimainclass.frmMain(root)


def printuj(Event=None):
    print("tekst")


print(form)
form.btnSortSquares.bind('<1>', printuj)

root.mainloop()
