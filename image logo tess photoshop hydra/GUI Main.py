#  Copyright (c) Filip Gogic 2022.

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tooltip


def drop_folder(event):
    # tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folderStringVar.set(filedialog.askdirectory())
    return


def drop_template(event):
    # tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    templateStringVar.set(
        filedialog.askopenfile(filetypes=(
            ("jpg,png,jpeg files", "*.jpg   *.png   *.jpeg"), ("png files", '*.png'))).name)
    return


root = Tk()
root.title('F I L I P')
root.resizable(True, False)
# root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frm = ttk.Frame(root, padding=10)
frm.grid(row=0, column=0, sticky=NSEW)

grid = Frame(frm)
grid.grid(sticky=NSEW, column=0, row=5, columnspan=2)

# frm.rowconfigure(7, weight=1)
# frm.columnconfigure(1, weight=1)

ttk.Label(frm, text="Right click to select folder/template").grid(column=1, row=0, pady=20)

ttk.Label(frm, text="Path to folder: ").grid(column=0, row=2, pady=10, sticky=W)
folderStringVar = StringVar()
txtPathToFolder = ttk.Entry(frm, textvariable=folderStringVar)
txtPathToFolder.grid(column=1, row=2, columnspan=2, sticky=EW)

ttk.Label(frm, text="Path to template: ").grid(column=0, row=3, pady=10, sticky=W)
templateStringVar = StringVar()
txtPathToTemplate = ttk.Entry(frm, textvariable=templateStringVar)
txtPathToTemplate.grid(column=1, row=3, columnspan=2, sticky=EW)

btnSortSquares = ttk.Button(frm, text="Sort squares")
btnSortSquares.grid(column=0, row=4, pady=10, sticky=W)
btnAddTemplate = ttk.Button(frm, text="Add template")
btnAddTemplate.grid(column=1, row=4)
btnSortGoodBad = ttk.Button(frm, text="Sort Good/Bad")
btnSortGoodBad.grid(column=2, row=4)

chkBtnIntVar = IntVar()
chkBtnOpenPS = ttk.Checkbutton(frm, text="Open PS", variable=chkBtnIntVar, onvalue=1, offvalue=0)
chkBtnOpenPS.grid(column=0, row=5, sticky=W)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=6, pady=20)

frm.columnconfigure(1, weight=1)
# frm.rowconfigure(tuple(range(5)), weight=1)

txtPathToFolder.bind('<3>', drop_folder)
txtPathToTemplate.bind('<3>', drop_template)

tooltipBtnSquare = tooltip.CreateToolTip(btnSortSquares,
                                         'Move square pictures to new folder - Squares')
tooltipBtnAddTemplate = tooltip.CreateToolTip(btnAddTemplate,
                                              'Add selected template to pictures (1000x1000 only). '
                                              'Pictures are stored in folder - Done')
tooltipBtnSortGoodBad = tooltip.CreateToolTip(btnSortGoodBad,
                                              'EXPERIMENTAL')
tooltipChkBtnPS = tooltip.CreateToolTip(chkBtnOpenPS,
                                        'Open NON square pictures in Photoshop')

root.mainloop()
