from PIL import Image, ImageOps
import pytesseract

image_path = 'C:/Users/Gogic/Desktop/test/1.jpg'
template_path = 'C:/Users/Gogic/Desktop/test/template.png'

template = Image.open(template_path)
image = Image.open(image_path).convert(mode='RGBA')
print(image.mode)
new_image = Image.composite(image, template, template)
new_image.show()
# thresh = 200
# fn = lambda x: 255 if x > thresh else 0
# image = image.convert('L').point(fn, mode='1')
#
#
# top_left = image.crop((0, 0, 185, 185))
# top_left = top_left.rotate(-90)
# top_left.show()
# bottom = image.crop((0, 850, 1000, 1000))

# s1 = pytesseract.image_to_string(top_left)
# s2 = pytesseract.image_to_string(bottom, config='--psm 11')

s1 = pytesseract.image_to_string(new_image, config='--psm 11')
print(s1)

# image.close()
#
# if s1.strip() or s2.strip():
#     print(s1, s2)
# else:
#     print('prazno')
