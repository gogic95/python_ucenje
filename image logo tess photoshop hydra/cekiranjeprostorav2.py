#  Copyright (c) Filip Gogic 2022.

import pytesseract
# from PIL import Image
# import pathlib
# import os


def cekiranje(image):

    # src_directory = os.path.join(src_directory_old, 'Squares')
    # dest_good_directory = os.path.join(src_directory, 'Good')
    # dest_bad_directory = os.path.join(src_directory, 'Bad')
    #
    # try:
    #     os.makedirs(dest_good_directory)  # create Good destination directory
    # except OSError:
    #     # The directory already existed, nothing to do
    #     pass
    #
    # try:
    #     os.makedirs(dest_bad_directory)  # create Bad destination directory
    # except OSError:
    #     # The directory already existed, nothing to do
    #     pass

    # if path.is_file() and path.name.endswith('.png') or path.name.endswith('.jpg') or path.name.endswith('.jpeg'):

    # image = Image.open(path)
    top_left = image.crop((0, 0, 185, 185))
    bottom = image.crop((0, 850, 1000, 1000))

    s1 = pytesseract.image_to_string(top_left)
    s2 = pytesseract.image_to_string(bottom)

    # image.close()

    if s1.strip() or s2.strip():
        return True
    else:
        return False
