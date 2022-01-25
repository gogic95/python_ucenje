import pathlib
from PIL import Image
import os

src_directory = pathlib.Path().resolve()
dest_directory = os.path.join(src_directory, 'Done')
template_image = Image.open('C:/Users/Gogic/Desktop/moji programi/python/PythonUcenje/za ogija/Squares/template.png')


try:
    os.makedirs(dest_directory)  # create destination directory
except OSError:
    # The directory already existed, nothing to do
    pass

for path in pathlib.Path(src_directory).iterdir():
    if path.is_file() and path.name.endswith('.png') or path.name.endswith('.jpg') or path.name.endswith('.jpeg'):
        image = Image.open(path)
        finished_image = image.copy()
        finished_image.paste(template_image, (0, 0), template_image)
        finished_image.save(dest_directory + '/done' + path.name, quality=95)
        image.close()

template_image.close()
