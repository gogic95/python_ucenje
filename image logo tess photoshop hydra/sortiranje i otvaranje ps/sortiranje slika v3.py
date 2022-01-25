import pathlib
from PIL import Image
import os
import win32com.client

src_directory = pathlib.Path().resolve()
dest_directory = os.path.join(src_directory, 'Squares')

try:
    os.makedirs(dest_directory)  # create destination directory
except OSError:
    # The directory already existed, nothing to do
    pass

for path in pathlib.Path(src_directory).iterdir():
    if path.is_file() and path.name.endswith('.png') or path.name.endswith('.jpg') or path.name.endswith('.jpeg'):
        image = Image.open(path)
        width, height = image.size
        image.close()
        if width == height:
            os.rename(path, os.path.join(dest_directory, path.name))
        else:
            win32com.client.Dispatch("Photoshop.Application").Open(path)
