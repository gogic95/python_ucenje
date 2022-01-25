import pathlib

from PIL import Image


for path in pathlib.Path("/PythonUcenje/za ogija/").iterdir():
    if path.is_file():
        current_file = open(path, "r")
        if current_file.name.endswith('.png') or current_file.name.endswith('.jpg'):
            image = Image.open('template.png')
            width, height = image.size
            print(width, height)
        current_file.close()
