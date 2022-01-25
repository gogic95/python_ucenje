import time
import pyautogui
import pytesseract
# from PIL import Image

j = 1
while 1:
    screenshot1 = pyautogui.screenshot(region=(473, 161, 691, 215))
    screenshot2 = pyautogui.screenshot(region=(473, 384, 691, 225))
    screenshot3 = pyautogui.screenshot(region=(473, 614, 691, 225))
    skup = (screenshot1, screenshot2, screenshot3)

    for sc in skup:
        tekst = pytesseract.image_to_string(sc)
        for i in range(0, len(tekst)):
            if tekst[i] == '%':
                if int(tekst[i - 2: i]) > 11:
                    sc.save('skrinsotovi/ekran' + str(j) + '.jpg')
                    j = j + 1

    time.sleep(15)