import time
from tkinter import *
import pyautogui
import pytesseract


class Brojac:
    br = 0

    #def __call__(self):
    #    Brojac.br += 1


minimeni = Tk()
minimeni.geometry('250x150')
labela = Label(minimeni, text='Broj meceva: '+str(Brojac.br), pady=40, padx=40)
labela.pack()


def fun():
    j = 1
    while 1:
        screenshot1 = pyautogui.screenshot(region=(473, 161, 691, 225))
        screenshot2 = pyautogui.screenshot(region=(473, 384, 691, 230))
        screenshot3 = pyautogui.screenshot(region=(473, 614, 691, 230))
        skup = (screenshot1, screenshot2, screenshot3)

        for sc in skup:
            tekst = pytesseract.image_to_string(sc)
            for i in range(0, len(tekst)):
                if tekst[i] == '%':
                    if int(tekst[i - 2: i]) > 14:
                        sc.save('skrinsotovi/ekran' + str(j) + '.jpg')
                        j += 1
                        # Brojac.br += 1

        time.sleep(15)


dugme = Button(minimeni, command=fun, text='start', pady=30)
dugme.pack(side=TOP)
minimeni.mainloop()
