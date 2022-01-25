#  Copyright (c) Filip Gogic 2022.

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tooltip


class frmMain(object):

    btnSortSquares = None

    def __init__(self, root):
        # self.root = Tk()
        self.root = root
        self.root.title('F I L I P')
        self.root.resizable(True, False)
        # root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid(row=0, column=0, sticky=NSEW)

        self.grid = Frame(self.frm)
        self.grid.grid(sticky=NSEW, column=0, row=5, columnspan=2)

        # frm.rowconfigure(7, weight=1)
        # frm.columnconfigure(1, weight=1)

        ttk.Label(self.frm, text="Right click to select folder/template").grid(column=1, row=0, pady=20)

        ttk.Label(self.frm, text="Path to folder: ").grid(column=0, row=2, pady=10, sticky=W)
        self.folderStringVar = StringVar()
        self.txtPathToFolder = ttk.Entry(self.frm, textvariable=self.folderStringVar)
        self.txtPathToFolder.grid(column=1, row=2, columnspan=2, sticky=EW)

        ttk.Label(self.frm, text="Path to template: ").grid(column=0, row=3, pady=10, sticky=W)
        self.templateStringVar = StringVar()
        self.txtPathToTemplate = ttk.Entry(self.frm, textvariable=self.templateStringVar)
        self.txtPathToTemplate.grid(column=1, row=3, columnspan=2, sticky=EW)

        self.btnSortSquares = ttk.Button(self.frm, text="Sort squares")
        self.btnSortSquares.grid(column=0, row=4, pady=10, sticky=W)
        self.btnAddTemplate = ttk.Button(self.frm, text="Add template")
        self.btnAddTemplate.grid(column=1, row=4)
        self.btnSortGoodBad = ttk.Button(self.frm, text="Sort Good/Bad")
        self.btnSortGoodBad.grid(column=2, row=4)

        self.chkBtnIntVar = IntVar()
        self.chkBtnOpenPS = ttk.Checkbutton(self.frm, text="Open PS", variable=self.chkBtnIntVar, onvalue=1, offvalue=0)
        self.chkBtnOpenPS.grid(column=0, row=5, sticky=W)

        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=1, row=6, pady=20)

        self.frm.columnconfigure(1, weight=1)
        # frm.rowconfigure(tuple(range(5)), weight=1)

        self.txtPathToFolder.bind('<3>', self.drop_folder)
        self.txtPathToTemplate.bind('<3>', self.drop_template)

        tooltip.CreateToolTip(self.btnSortSquares, 'Move square pictures to new folder - Squares')
        tooltip.CreateToolTip(self.btnAddTemplate, 'Add selected template to pictures (1000x1000 only). '
                                                   'Pictures are stored in folder - Done')
        tooltip.CreateToolTip(self.btnSortGoodBad, 'EXPERIMENTAL')
        tooltip.CreateToolTip(self.chkBtnOpenPS, 'Open NON square pictures in Photoshop')

        # self.root.mainloop()

    def drop_folder(self, event=None):
        # tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
        self.folderStringVar.set(filedialog.askdirectory())

    def drop_template(self, event=None):
        # tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
        self.templateStringVar.set(
            filedialog.askopenfile(filetypes=(
                ("jpg,png,jpeg files", "*.jpg   *.png   *.jpeg"), ("png files", '*.png'))).name)
