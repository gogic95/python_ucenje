import pathlib
from PIL import Image
import os

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
        print(str(path))
        if width == height:
            os.rename(path, os.path.join(dest_directory, path.name))

