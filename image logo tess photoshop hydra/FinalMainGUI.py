#  Copyright (c) Filip Gogic 2022.

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import filedialog
import tooltip
import sortiranjeslikav4


# import cekiranjeprostorav2
# import ubacivanjelogotipav2


def drop_folder(event=None):
    # tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folderStringVar.set(filedialog.askdirectory())
    return


def drop_template(event=None):
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

ttk.Label(frm, text="Right click to select folder/template").grid(column=1, row=0, pady=20, sticky=W)

ttk.Label(frm, text="Path to folder: ").grid(column=0, row=2, pady=10, sticky=W)
folderStringVar = StringVar()
txtPathToFolder = ttk.Entry(frm, textvariable=folderStringVar)
txtPathToFolder.grid(column=1, row=2, columnspan=2, sticky=EW)
btnPathToFolder = ttk.Button(frm, text="+", command=drop_folder, style='Bold.TButton')
btnPathToFolder.grid(column=3, row=2, sticky=W)

ttk.Label(frm, text="Path to template: ").grid(column=0, row=3, pady=10, sticky=W)
templateStringVar = StringVar()
txtPathToTemplate = ttk.Entry(frm, textvariable=templateStringVar)
txtPathToTemplate.grid(column=1, row=3, columnspan=2, sticky=EW)
btnPathToTemplate = ttk.Button(frm, text="+", command=drop_template, style='Bold.TButton')
btnPathToTemplate.grid(column=3, row=3, sticky=W)


def beginAutomation():
    folderPath = folderStringVar.get()
    templatePath = templateStringVar.get()
    chkBtn = chkBtnIntVar.get()  # 1 Checked, 0 Unchecked

    if not folderPath or not templatePath:
        tkinter.messagebox.showerror(title='Error', message='Folder or Template path is empty!')
        return

    sortiranjeslikav4.sortiranjeSlika(folderPath, chkBtn, templatePath)
    # cekiranjeprostorav2.cekiranje(folderPath)
    # ubacivanjelogotipav2.ubacivanje(folderPath, templatePath)


boldStyle = ttk.Style()
boldStyle.configure("Bold.TButton", font=('Arial', '12', 'bold'))
btnMagic = ttk.Button(frm, text="MAGIC!", command=beginAutomation, style='Bold.TButton')
btnMagic.grid(column=0, row=4, columnspan=4, pady=10, sticky=EW)

chkBtnIntVar = IntVar()
chkBtnOpenPS = ttk.Checkbutton(frm, text="Open Photoshop", variable=chkBtnIntVar, onvalue=1, offvalue=0)
chkBtnOpenPS.grid(column=0, row=5, sticky=W)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=6, pady=20, sticky=E)

frm.columnconfigure(1, weight=1)
# frm.rowconfigure(tuple(range(5)), weight=1)

txtPathToFolder.bind('<3>', drop_folder)
txtPathToTemplate.bind('<3>', drop_template)

tooltipBtnSquare = tooltip.CreateToolTip(btnMagic,
                                         'Let the magic begin!')

tooltipChkBtnPS = tooltip.CreateToolTip(chkBtnOpenPS,
                                        'Open NON square pictures in Photoshop')

root.mainloop()
