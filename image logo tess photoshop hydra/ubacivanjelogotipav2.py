#  Copyright (c) Filip Gogic 2022.

from PIL import Image


def ubacivanje(image, template_path):

    # src_directory = os.path.join(src_directory_old, 'Squares/Good')
    # dest_directory = os.path.join(src_directory, 'Done')
    template_image = Image.open(template_path)

    # try:
    #     os.makedirs(dest_directory)  # create destination directory
    # except OSError:
    #     # The directory already existed, nothing to do
    #     pass

    # for path in pathlib.Path(src_directory).iterdir():
    #     if path.is_file() and path.name.endswith('.png') or path.name.endswith('.jpg') or path.name.endswith('.jpeg'):
    #         image = Image.open(path)

    finished_image = image.copy()
    finished_image = finished_image.convert(mode='RGBA')
    finished_image.alpha_composite(template_image)
    finished_image = finished_image.convert(mode='RGB')
    # finished_image.paste(template_image, (0, 0), template_image)
    # finished_image.save(dest_directory + '/done' + path.name, quality=95)
    # image.close()

    template_image.close()
    return finished_image
