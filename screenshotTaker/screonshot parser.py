import os

import pytesseract
from PIL import Image

s = pytesseract.image_to_string(Image.open('skrinsotovi/ekran1.jpg'))

for i in range(0, len(s)):
    if s[i] == '%':
        n = s[i-2: i]


print(n)
# if int(n) < 40:
    # os.startfile('C:/Users/Gogic/Desktop/moji programi/python/PythonUcenje/screenshotTaker/skrinsotovi/ekran200.jpg')
# else:
    # os.startfile('C:/Users/Gogic/Desktop/moji programi/python/PythonUcenje/screenshotTaker/skrinsotovi/ekran1.jpg')
